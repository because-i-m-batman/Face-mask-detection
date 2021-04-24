from flask import Flask,jsonify,request
from fac_mask_detector import run_face_mask_detection

app = Flask(__name__)

@app.route('/send_input', methods=['POST'])
def send_input_image_to_model():
	file = request.files.get("image","")
	# print(file)
	run_face_mask_detection(file)
	return "file sent"

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5001)