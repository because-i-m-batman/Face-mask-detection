from flask import Flask,jsonify,request
from face_mask_detector import Face_Mask_Detection
import cv2
import numpy

app = Flask(__name__)

@app.route('/send_input', methods=['POST'])
def run_detection():

	file = request.files.get("image","")
	print('[INFO] Running Face Mask Detection.')
	input_image = cv2.imdecode(numpy.fromstring(file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
	output_image = Face_Mask_Detection.run_face_mask_detection(input_image)
	print('[INFO] Detection Successfully Done.')
	return "file sent"

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5001)