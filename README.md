# Technocrats TCR Task 1 
<details>
  <summary><b>Subtask 1 - Green Ball Detection</b></summary><br>
  
[![Language Used](https://img.shields.io/badge/language%20used-python-orange)](https://github.com/hariketsheth/TCR_Task_1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [![Module Integration](https://img.shields.io/badge/python--module-OpenCV-blue)](https://github.com/hariketsheth/TCR_Task_1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   [![Build Status](https://img.shields.io/badge/build-passing-green)](https://github.com/hariketsheth/TCR_Task_1)


## Description
Developed First Module that takes video feeds from the camera and detects the green ball.

## Python Modules Used:
- OpenCV 

## Implementation 
- Using cv2.VideoCapture() to get a live video capture object for the camera. 
            ```
            self.camera = cv.VideoCapture(0)
            ```
            
- Using the read() method to read the frames.
            ```
            response, frame = self.camera.read()
            ```
- Take each frame of the video
           
- Converting it from BGR to HSV color-space
           ```
            frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            ```
- Then, threshold the HSV image for a range of green color
            ```
            green_L_hsv = (36, 86, 6)
            ```
            ```
            green_U_hsv = (86, 255, 255)
            ```
- Extract the Green object alone.
            ```
            green_extract = cv.inRange(frame_hsv,green_L_hsv,green_U_hsv)
            ```
- Enhancing the Object mask by Image Processing - Erode() and Dilation()
            ```
            green_extract = cv.erode(green_extract, None, iterations=2)
            ```
            ```
            green_extract = cv.dilate(green_extract, None, iterations=2)
            ```
- For the contour / outline of the Green Ball, using findContours()
            ```
            boundary, hierarchy= cv.findContours(green_extract.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
            ```
- Outlining the Green Object Area in the shape of a circle
            ```
            cv.circle(frame, (int(x), int(y)), int(radius),(255, 255, 255), 5)
            ```
- Using cv2.imshow() method to show the frames in the video.
            ```
            cv.imshow("window1",frame)
            ```
            ```
            cv.imshow("window2", green_extract)
            ```
- Breaking the infinite loop when the user clicks specific key 'd'.
            ```
            if cv.waitKey(1) & 0xFF == ord('d'):
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

## Implementation 

## Testing
![Team4-Testing](https://github.com/hariketsheth/TCR_Task_1/blob/main/templates/Team4-Testing.gif)


</details>
