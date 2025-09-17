
# main.py

import cv2
import face_recognition
import pickle
import uuid
import os
import numpy as np
import time
from database import create_tables, insert_unique_person, insert_detection, get_all_encodings

# Setup
create_tables()

known_encodings = []
known_ids = []
registered_names = set()

# Load registered face images
registered_folder = 'registered_faces'
photo_dir = 'person_photos'
os.makedirs(photo_dir, exist_ok=True)

for filename in os.listdir(registered_folder):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        name = os.path.splitext(filename)[0]
        path = os.path.join(registered_folder, filename)
        img = face_recognition.load_image_file(path)
        enc = face_recognition.face_encodings(img)
        if enc:
            known_encodings.append(enc[0])
            known_ids.append(name)
            registered_names.add(name)
            print(f"✅ Registered face loaded (awaiting detection): {name}")

# Create set for tracking detected registered persons
registered_detected_ids = set()

# Load previously saved encodings from database
for person_id, enc in get_all_encodings():
    known_encodings.append(pickle.loads(enc))
    known_ids.append(person_id)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

def get_face_encoding(frame):
    if frame is None or frame.size == 0:
        return [], []
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)
    return boxes, encodings

currently_visible_ids = set()
last_detection_time = {}
recent_unmatched_encodings = []
DETECTION_INTERVAL = 10

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    h, w = frame.shape[:2]
    roi_margin_w = int(w * 0.1)
    roi_margin_h = int(h * 0.1)
    roi_top_left = (roi_margin_w, roi_margin_h)
    roi_bottom_right = (w - roi_margin_w, h - roi_margin_h)
    cv2.rectangle(frame, roi_top_left, roi_bottom_right, (0, 255, 0), 2)

    boxes, encodings = get_face_encoding(frame)
    visible_ids = set()

    for encoding, box in zip(encodings, boxes):
        top, right, bottom, left = box

        # ROI check
        if not (left >= roi_top_left[0] and top >= roi_top_left[1] and
                right <= roi_bottom_right[0] and bottom <= roi_bottom_right[1]):
            print("⚠️ Face outside ROI. Skipping.")
            continue

        # Image quality checks2
        face_crop = frame[top:bottom, left:right]
        fh, fw = face_crop.shape[:2]
        gray_crop = cv2.cvtColor(face_crop, cv2.COLOR_BGR2GRAY)
        laplacian_var = cv2.Laplacian(gray_crop, cv2.CV_64F).var()
        aspect_ratio = fw / fh if fh > 0 else 0

        if laplacian_var < 100 or not (0.80 < aspect_ratio < 1.25) or fh < 55 or fw < 55:
            print(f"⚠️ Skipping: Blurry or too small. Var: {laplacian_var:.2f}, Ratio: {aspect_ratio:.2f}")
            continue

        # Side face detection
        face_landmarks = face_recognition.face_landmarks(face_crop)
        if face_landmarks:
            landmarks = face_landmarks[0]
            left_eye = np.mean(landmarks['left_eye'], axis=0)
            right_eye = np.mean(landmarks['right_eye'], axis=0)
            nose = np.mean(landmarks['nose_bridge'], axis=0)

            eye_distance = np.linalg.norm(left_eye - right_eye)
            eye_nose_distance = np.linalg.norm(((left_eye + right_eye) / 2) - nose)

            if eye_distance < 0.5 * eye_nose_distance:
                print("⚠️ Side face detected. Skipping.")
                continue
        else:
            print("⚠️ No facial landmarks detected. Skipping.")
            continue

        person_id = None
        name = "Unknown"
        current_time = time.time()
        MATCH_THRESHOLD = 0.48      # For perfect confident match
        UNKNOWN_THRESHOLD = 0.58    # If distance > this → treat as unknown

        distances = face_recognition.face_distance(known_encodings, encoding)

        if len(distances) > 0:
            best_index = np.argmin(distances)
            min_distance = distances[best_index]
            print(f"🧪 Min distance: {min_distance:.2f} (ID: {known_ids[best_index]})")

            if min_distance < MATCH_THRESHOLD:
                # ✅ Confident match
                person_id = known_ids[best_index]
                visible_ids.add(person_id)

                if person_id in registered_names and person_id not in registered_detected_ids:
                    insert_unique_person(person_id, person_id, pickle.dumps(encoding))
                    registered_detected_ids.add(person_id)
                    print(f"✅ Registered person detected: {person_id}")

                if person_id not in last_detection_time or \
                time.time() - last_detection_time[person_id] >= DETECTION_INTERVAL:
                    insert_detection(person_id)
                    last_detection_time[person_id] = time.time()
                    print(f"📍 Detection recorded: {person_id}")

                currently_visible_ids.add(person_id)
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, person_id, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                continue

            elif min_distance > UNKNOWN_THRESHOLD:
                print("🆕 New unknown person detected (distance too high) → will register")
                # **No continue here** — proceed to registration flow immediately

            else:
                print("🤔 Uncertain match, but still treating as unknown to avoid false match")
                # **No continue here** — proceed to registration flow immediately

        # Recently seen unknown face check
        skip_registration = any(np.linalg.norm(old - encoding) < 0.4 for old in recent_unmatched_encodings)
        if skip_registration:
            print("⚠️ Recently seen unknown person. Skipping.")
            continue

        # Register new unknown person
        # Now proceed to register unknown person
        person_id = str(uuid.uuid4())[:8]
        name = f"Visitor-{len(known_ids) + 1}"
        visible_ids.add(person_id)
        currently_visible_ids.add(person_id)

        photo_path = os.path.join(photo_dir, f"{person_id}.jpg")
        cv2.imwrite(photo_path, face_crop)
        print(f"📷 New face saved: {photo_path}")

        known_encodings.append(encoding)
        known_ids.append(person_id)

        insert_unique_person(person_id, name, pickle.dumps(encoding))
        insert_detection(person_id)
        last_detection_time[person_id] = time.time()
        print(f"✅ New person registered: {name} (ID: {person_id})")

        recent_unmatched_encodings.append(encoding)
        if len(recent_unmatched_encodings) > 10:
            recent_unmatched_encodings.pop(0)

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, "Registering...", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    currently_visible_ids.intersection_update(visible_ids)

    cv2.imshow("Multi-Person Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

