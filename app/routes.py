from collections import defaultdict

import cv2
import numpy as np
import requests
from flask import jsonify, request

from app import app
from app import utils


@app.route("/", methods=["GET"])
def root():
    return "Page default"


@app.route('/predicted', methods=['POST'])
def upload_file():
    try:
        urls = request.json.get('urls')

        if not urls or not isinstance(urls, list):
            return jsonify({"message": "No URLs provided or incorrect format", "status": "fail"}), 400

        images_by_class = defaultdict(list)

        for url in urls:
            response = requests.get(url)
            if response.status_code != 200:
                return jsonify({"message": f"Failed to fetch image from {url}", "status": "fail"}), 400

            file_data = response.content
            nparr = np.frombuffer(file_data, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if image is None:
                return jsonify({"error": f"Failed to decode image from {url}. Ensure correct format."}), 500

            predicted_class = utils.predict_class(image)
            images_by_class[predicted_class].append(url)

        return jsonify({
            "message": "URLs successfully processed and predicted",
            "status": "success",
            "images_by_class": images_by_class
        })

    except Exception as e:
        return jsonify({"error": f"Failed to upload file: {str(e)}"}), 500

