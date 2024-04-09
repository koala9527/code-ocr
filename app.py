from flask import Flask, request, jsonify
from ddddocr import DdddOcr

app = Flask(__name__)

ocr = DdddOcr(beta=True)

@app.route("/ocr", methods=["POST"])
def ocr_image():
    image = request.files["image"]
    res = ocr.classification(image.read())
    print(res)
    return jsonify(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)