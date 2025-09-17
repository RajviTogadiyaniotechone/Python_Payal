from flask import Flask, render_template, request, jsonify, url_for
import json
import dicttoxml
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/beautify', methods=['POST'])
def beautify_json():
    try:
        data = request.get_json(force=True)  # Ensures JSON is parsed properly
        formatted_json = json.dumps(data, indent=4)
        return jsonify({"beautified_json": formatted_json})
    except json.JSONDecodeError as e:
        return jsonify({"error": "Invalid JSON format", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

@app.route('/minify', methods=['POST'])
def minify_json():
    try:
        data = request.get_json(force=True)
        minified_json = json.dumps(data, separators=(',', ':'))
        return jsonify({"minified_json": minified_json})
    except json.JSONDecodeError as e:
        return jsonify({"error": "Invalid JSON format", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

@app.route('/validate', methods=['POST'])
def validate_json():
    try:
        json.loads(request.data)
        return jsonify({"message": "✅ JSON is valid!"})
    except json.JSONDecodeError as e:
        return jsonify({"error": "❌ Invalid JSON format!", "details": str(e)}), 400

@app.route('/convert-to-xml', methods=['POST'])
def convert_to_xml():
    try:
        data = request.get_json(force=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON must be an object"}), 400

        xml_data = dicttoxml.dicttoxml(data, custom_root="root", attr_type=False).decode("utf-8")
        return jsonify({"xml": xml_data})

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400
    except Exception as e:
        return jsonify({"error": "Conversion failed", "details": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
