from flask import Flask, render_template, request, jsonify
import json
from jsonschema import validate, ValidationError
import hashlib
import dicttoxml
import xmltodict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/format', methods=['POST'])
def format_json():
    try:
        data = request.json.get('jsonData', '')
        parsed_json = json.loads(data)  
        beautified_json = json.dumps(parsed_json, indent=4)  
        return jsonify({"success": True, "formatted_json": beautified_json})
    except json.JSONDecodeError as e:
        return jsonify({"success": False, "error": str(e)})


@app.route('/convert-json', methods=['POST'])
def convert_xml_to_json():
    try:
        xml_data = request.json.get("xmlData", "").strip()
        json_data = json.dumps(xmltodict.parse(xml_data), indent=4)
        return jsonify(success=True, json=json_data)
    except Exception as e:
        print(f"XML to JSON Conversion Error: {str(e)}")  # Log error
        return jsonify(success=False, error=str(e))

@app.route('/minify', methods=['POST'])
def minify_json():
    try:
        data = request.json.get('jsonData', '')
        parsed_json = json.loads(data)
        minified_json = json.dumps(parsed_json, separators=(',', ':'))  
        return jsonify({"success": True, "minified_json": minified_json})
    except json.JSONDecodeError as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/convert-xml', methods=['POST'])
def convert_to_xml():
    try:
        data = request.json.get('jsonData', '')
        parsed_json = json.loads(data)
        xml_data = dicttoxml.dicttoxml(parsed_json).decode()
        return jsonify({"success": True, "xml": xml_data})
    except json.JSONDecodeError as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/generate-link', methods=['POST'])
def generate_link():
    data = request.json.get('jsonData', '')
    hash_key = hashlib.md5(data.encode()).hexdigest()
    link = f"http://localhost:5001/shared/{hash_key}"
    return jsonify({"success": True, "link": link})


@app.route('/validate', methods=['POST'])
def validate_json():
    try:
        json_data = request.json.get('jsonData', '')
        schema_data = request.json.get('schemaData', '')

        parsed_json = json.loads(json_data)
        parsed_schema = json.loads(schema_data)

        validate(instance=parsed_json, schema=parsed_schema)
        return jsonify({"success": True, "message": "JSON is valid against the schema ✅"})
    except ValidationError as e:
        return jsonify({"success": False, "error": f"Schema Validation Error: {e.message}"})
    except json.JSONDecodeError as e:
        return jsonify({"success": False, "error": f"Invalid JSON: {e}"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  
