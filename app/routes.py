from flask import jsonify, request
from app import app
import base64
import cv2
import numpy as np
from app import utils

@app.route("/", methods=["GET"])
def root():
    return "Page default"


@app.route('/predicted', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({"message": "No file part in the request", "status": "fail"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"message": "No selected file", "status": "fail"}), 400

        file_data = file.read()

        nparr = np.frombuffer(file_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None:
            return jsonify({"error": "Failed to decode image. Ensure correct format."}), 500

        predicted_class = utils.predict_class(image)

        return jsonify({
            "message": "File successfully uploaded and predicted",
            "status": "success",
            "predicted_class": predicted_class
        })

    except Exception as e:
        return jsonify({"error": f"Failed to upload file: {str(e)}"}), 500

