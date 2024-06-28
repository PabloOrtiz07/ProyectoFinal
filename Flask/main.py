from flask import Flask, jsonify, request
import utils  # Importing the utils module
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return "Test"

UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part in the request", "status": "fail"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"message": "No selected file", "status": "fail"}), 400

    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return jsonify({
            "message": "File successfully uploaded",
            "file_path": file_path,
            "status": "success"
        })

    return jsonify({"message": "File upload failed", "status": "fail"}), 400


@app.route("/OutPut", methods=["GET"])
def utils_sample():
    img_path = request.args.get('img_path')
    if not img_path:
        return jsonify({"error": "img_path parameter is required"}), 400
    
    try:
        predicted_class = utils.predict_class(img_path)
        return jsonify({"predicted_class": predicted_class})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

