<!-- ================= BACKEND (PYTHON – FLASK) =================
SAVE THIS AS app.py
--------------------------------------------------
from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)

ROBOFLOW_API_KEY = "RJVsuf7wVUXCCYtfuawt"
MODEL = "traffic-detection/1"   # change to your model

@app.route('/detect', methods=['POST'])
def detect():
    image = request.files['image']
    encoded = base64.b64encode(image.read()).decode('utf-8')

    url = f"https://serverless.roboflow.com api_key="RJVsuf7wVUXCCYtfuawt"
    response = requests.post(url, data=encoded, headers={"Content-Type": "application/x-www-form-urlencoded"})

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
--------------------------------------------------
INSTALL REQUIREMENTS:
  pip install flask requests

RUN:
  python app.py
================================================== -->
