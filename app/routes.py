from flask import jsonify, request
from app import app, db
from app.models import UploadedFile
import base64
import cv2
import numpy as np
from app import utils

@app.before_request
def create_tables():
    db.create_all()

@app.route("/", methods=["GET"])
def root():
    return "Page default"

@app.route('/Input', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({"message": "No file part in the request", "status": "fail"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"message": "No selected file", "status": "fail"}), 400

        file_data = file.read()
        encoded_data = base64.b64encode(file_data)

        new_file = UploadedFile(filename=file.filename, data=encoded_data)
        db.session.add(new_file)
        db.session.commit()

        return jsonify({
            "message": "File successfully uploaded",
            "file_id": new_file.id,
            "status": "success"
        })

    except Exception as e:
        return jsonify({"error": f"Failed to upload file: {str(e)}"}), 500

@app.route("/Output/<int:file_id>", methods=["GET"])
def utils_sample(file_id):
    try:
        file = UploadedFile.query.get(file_id)
        if not file:
            return jsonify({"error": "File not found"}), 404

        img_data = base64.b64decode(file.data)

        nparr = np.frombuffer(img_data, np.uint8)

        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None:
            return jsonify({"error": "Failed to decode image. Ensure correct format."}), 500

        predicted_class = utils.predict_class(image)

        return jsonify({"predicted_class": predicted_class})

    except Exception as e:
        print(f"Error processing file {file_id}: {str(e)}")
        return jsonify({"error": f"Error processing file: {str(e)}"}), 500
