# Face-mask-detection

## How to Run

1. Prerequisites:
-	Installed Docker
-	Installed Docker-compose

2. Run this Command on Terminal 1 or your host machine: 
{ ``` }

	docker-compose up 

```
3. Send post request (send images as to the model):

a. Open another Terminal and run this following command to send the image to the model:

	import requests
	url = 'where you want to host the app'(for local machine <localhost:5001/send_input>)
	files = {'image': open('<input-image-path>', 'rb')}
	resp = requests.post(url, files=files)


b. convert json response to image array ,after above commands use these commands:

	import json
	import numpy as np
	json_load = json.loads(resp.text)
	output_image_array = np.asarray(json_load["output_image"])

# output

out.jpg is the demo output image of 3.jpg
