# Technocrats TCR Task 1 
<details>
  <summary><b>Subtask 1 - Green Ball Detection</b></summary><br>
  
[![Language Used](https://img.shields.io/badge/language%20used-python-orange)](https://github.com/hariketsheth/TCR_Task_1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [![Module Integration](https://img.shields.io/badge/python--module-OpenCV-blue)](https://github.com/hariketsheth/TCR_Task_1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   [![Build Status](https://img.shields.io/badge/build-passing-green)](https://github.com/hariketsheth/TCR_Task_1)


## Description
Developed First Module that takes video feeds from the camera and detects the green ball.

## Python Modules Used:
- OpenCV 

## Installation & Usage
- For Installation:
Use the following command. 
```
pip install opencv-python
```
- Usage:
```python
import cv2 as cv
# Or Simply, import the module as:
import cv2
```

## Implementation 
- Using cv2.VideoCapture() and read() getting a live video, and reading the frames. Converting them to HSV color-space
```python
self.camera = cv.VideoCapture(0)
response, frame = self.camera.read()
frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
```
<br>   

- Then, threshold the HSV image for a range of green color
```python
green_L_hsv = (39, 140, 50)
green_U_hsv = (80, 255, 255)
```
<br>

- Extract the Green object & Enhancing the Object mask by use of Erode() and Dilation()
```python
green_extract = cv.inRange(frame_hsv,green_L_hsv,green_U_hsv)
green_extract = cv.erode(green_extract, None, iterations=2)
green_extract = cv.dilate(green_extract, None, iterations=2)
```
<br>

- For the circular outline / boundary of the Green Ball, using findContours()
```python
boundary, hierarchy= cv.findContours(green_extract.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cv.circle(frame, (int(x), int(y)), int(radius),(255, 255, 255), 5)
```
<br>

- Using cv2.imshow() method to show the frames in the video until user presses 'd'.
```python
cv.imshow("window1",frame)
cv.imshow("window2", green_extract)
if cv.waitKey(1) & 0xFF == ord('d'):
  break
```
</details>
<hr>
<details>
  <summary><b>Subtask 2 - Integrating to Web Interface using Flask</b></summary><br><br>
  
[![Language Used](https://img.shields.io/badge/language%20used-python-orange)](https://github.com/hariketsheth/TCR_Task_1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [![Module Integration](https://img.shields.io/badge/python--module-OpenCV%2C%20Flask%2C%20Numpy-blue)](https://github.com/hariketsheth/TCR_Task_1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Build Status](https://img.shields.io/badge/build-passing-green)](https://github.com/hariketsheth/TCR_Task_1)


## Description
Used the Flask Module of Python to integrate Green Ball Detection script to a web interface

## Python Modules Used:
- OpenCV 
- Flask
- Numpy

## Installation & Usage
- For Installation:
Use the following commands.
```
pip install opencv-python
pip install flask
pip install numpy
```
- Usage:
```python
import cv2 as cv
import flask as fsk
import numpy as np
# Or Simply, import the modules as:
import cv2
import flask
import numpy
```

## Implementation
- Importing the camera module created in Subtask-1 and creating a Flask instance by passing `__name__` (name of the current Python Module).
```python
from camera import Video
import flask as fsk


app = fsk.Flask(__name__)
```
<br>

- Creating App Routes for Web Interface. 
- `@app.route('/')` denotes the Index/ Homepage. 
- The gen() function continuously returns frames from the camera. It calls the main_exec() method, and then it yields frame with a content type of image/jpeg.
```python
@app.route('/')
def index():
    return fsk.render_template('index.html')

def gen(camera):
    while True:
        frame = camera.main_exec()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
```
<br>

- The `/video_feed` route returns instance of the Camera to gen(). The mimetype argument is set to the multipart/x-mixed-replace.
- `mimetype='multipart/x-mixed-replace; boundary=frame` - This Mimetype replaces the previous frame and setting the boundary = frame
```python
@app.route('/video_feed')
def video_feed():
    return fsk.Response(gen(Video()),mimetype='multipart/x-mixed-replace; boundary=frame')
```
<br>

- Creating the App Routes for Getting the Font and Redirecting the WebPage to Github Repo. 
```python
@app.route('/font')
def font():
    filename = 'static/Azonix.otf'
    return fsk.send_file(filename, mimetype='font/otf')

@app.route('/github')
def github():
    return fsk.redirect("https://github.com/hariketsheth/TCR_Task_1")
```

<br>

- Running the Flask App using run()
```python
app.run(debug=True)
```
## Testing
![Team4-Testing](https://github.com/hariketsheth/TCR_Task_1/blob/main/templates/Team4-Testing.gif)


</details>
<hr>
<details>
  <summary><b>Subtask 3 - Displaying the status of the Green ball (Presence, Area Covered & Position)</b></summary><br><br>
  
[![Language Used](https://img.shields.io/badge/language%20used-python-orange)](https://github.com/hariketsheth/TCR_Task_1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [![Module Integration](https://img.shields.io/badge/python--module-OpenCV%2C%20Flask%2C%20Numpy-blue)](https://github.com/hariketsheth/TCR_Task_1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Build Status](https://img.shields.io/badge/build-passing-green)](https://github.com/hariketsheth/TCR_Task_1)


## Description
Integrating the Module created in Subtask-1 and displaying the status of the Green ball on the Web Interface created in Subtask-2

## Python Modules Used:
- OpenCV 
- Flask
- Numpy

## Installation & Usage
- For Installation:
Use the following commands.
```
pip install opencv-python
pip install flask
pip install numpy
```
- Usage:
```python
import cv2 as cv
import flask as fsk
import numpy as np
# Or Simply, import the modules as:
import cv2
import flask
import numpy
```

## Implementation
- If the 'area' recieved from the `camera.py` script is not NULL or 0.0 then we add "%" symbol to the value. Setting the `present` variable as FALSE initially.
```python
@app.route('/status')
def status():
    present = "FALSE"
    global area
    if area != '0.0' and area!="NULL":
        if " %" not in area:
            area+=" %"
    else:
        area = "NULL"
```
<br>

- If the position is not NULL, then it implies Green Ball is Present. Else the Green Ball is not present.
```python
    if (position!="NULL"):
        present = "TRUE"
    else:
        present = "FALSE"
    print(present, position, area)
    return fsk.jsonify(present = present, position = position, area = area)
```
<br>

- The parameters `present`, `area`, `position` recieved from `main.py` are shown in the Table using JQuery
```html
<tr>
	<td>Presence</td>
	<td id="present_f" style="color: #d9534f; font-weight: bolder;"></td>
	<td id="present_t" style="color: #5cb85c; font-weight: bolder;"></td>
</tr>
<tr>
	<td>Area</td>
	<td id="area_f" style="color: #d9534f; font-weight: bolder;"></td>
	<td id="area_t" style="color: #5cb85c; font-weight: bolder;"></td>
</tr>

<tr>
	<td>Nearest Corner</td>
	<td id="position_f" style="color: #d9534f; font-weight: bolder;"></td>
	<td id="position_t" style="color: #5cb85c; font-weight: bolder;"></td>
</tr>
```
<br>

- If the parameter "present" value is "FALSE", then the visibility of elements with ID "present_f, position_f, area_f" is changed to show() 
  - And the visibility of elements with ID "present_t, position_t, area_t" is set to hide()
- If the parameter "present" value is "TRUE", then the visibility of elements with ID "present_t, position_t, area_t" is changed to show()
  - And the visibility of elements with ID "present_f, position_f, area_f" is set to hide()
```js
<script>
  $(document).ready(function() {
     $.getJSON('/status' ,
        function(parameters) {
	if(parameters.present =="FALSE"){
           $("#present_f").text(parameters.present).show(); 
           $("#position_f").text(parameters.position).show();
           $("#area_f").text(parameters.area).show();
           $("#present_t").text(parameters.present).hide();
           $("#position_t").text(parameters.position).hide();
           $("#area_t").text(parameters.area).hide();
	}
	else{
	   $("#present_t").text(parameters.present).show();
	   $("#position_t").text(parameters.position).show();
	   $("#area_t").text(parameters.area).show();
	   $("#present_f").text(parameters.present).hide();
	   $("#position_f").text(parameters.position).hide();
	   $("#area_f").text(parameters.area).hide();
	}
     });
       setTimeout(arguments.callee, 500);
  });
</script>
```

## Testing


</details>
