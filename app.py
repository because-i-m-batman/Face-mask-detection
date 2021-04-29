from flask import Flask,jsonify,request,send_file,jsonify
from face_mask_detector import Face_Mask_Detection
import cv2
import numpy

app = Flask(__name__)
detector_object = Face_Mask_Detection()

@app.route('/send_input', methods=['GET','POST'])
def run_detection():

	file = request.files.get("image","")
	print('[INFO] Running Face Mask Detection.')
	input_image = cv2.imdecode(numpy.fromstring(file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
	# print(input_image)
	output_image = detector_object.run_face_mask_detection(input_image)
	print('[INFO] Detection Successfully Done.')
	# return send_file(output_image,mimetype='image/gif')
	return jsonify({"output_image":[output_image]})

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5001)