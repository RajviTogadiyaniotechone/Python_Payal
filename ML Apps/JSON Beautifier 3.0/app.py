from flask import Flask, request, jsonify, render_template
import json
import json5  # Helps parse JSON with minor errors
from flask_cors import CORS
import os

# Import GPT4All only if available
try:
    from gpt4all import GPT4All  
    AI_ENABLED = True
except ImportError:
    print("⚠ GPT4All library not found! AI features disabled.")
    AI_ENABLED = False

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow frontend to access backend

# Load AI model (if available)
ai_model = None
if AI_ENABLED:
    model_path = "E:/Payal Ramani/Apps/JSON Beautifier 3.0/models/mistral-7b-instruct-v0.1.Q4_0.gguf"
    
    if not os.path.exists(model_path):
        print(f"❌ Model not found at {model_path}")
    else:
        try:
            ai_model = GPT4All(model_path)
            print("✅ AI Model Loaded Successfully!")
        except Exception as e:
            print(f"❌ Error loading AI model: {e}")
            ai_model = None

# Function to beautify JSON
def beautify_json(json_str):
    """Formats JSON string into a readable format."""
    try:
        parsed_json = json5.loads(json_str)  # Accepts minor JSON errors
        return json.dumps(parsed_json, indent=4, sort_keys=True)
    except Exception as e:
        return f"Invalid JSON: {e}"

# Function to fix JSON using AI
def fix_json_with_ai(json_str):
    if ai_model is None:
        return "⚠ AI Model Not Loaded. Please check the model path."

    try:
        prompt = f"Fix this broken JSON and return only the corrected JSON:\n{json_str}"
        
        response = ai_model.generate(prompt, max_tokens=500)
        print("📢 AI Raw Response:", response)  # Debugging

        # Try parsing output to confirm validity
        fixed_json = json.loads(response)
        return json.dumps(fixed_json, indent=4)

    except json.JSONDecodeError:
        print("❌ AI returned invalid JSON:", response)
        return f"⚠ AI returned invalid JSON: {response}"
    
    except Exception as e:
        print(f"❌ AI Error: {e}")
        return f"⚠ AI Error: {e}"

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/beautify', methods=['POST'])
def beautify():
    """API to beautify JSON"""
    data = request.json.get("json", "")
    result = beautify_json(data)
    return jsonify({"result": result})

@app.route('/fix', methods=['POST'])
def fix():
    print("📢 Request received:", request.data)  # Debugging
    data = request.json.get("json", "")
    result = fix_json_with_ai(data)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
