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

## Testing


</details>
