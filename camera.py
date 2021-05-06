import cv2 as cv
import numpy as np

class Video (object):
    
    def __init__(self):
        self.camera = cv.VideoCapture(0)

    def __del__(self):
        self.camera.release()
 
    def main_exec(self):
        green_L_hsv = np.array([39, 140, 50])
        green_U_hsv = np.array([80, 255, 255])
        while True:
            response, frame = self.camera.read()
            if frame is None:
                break

            frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            frame_hsv = cv.medianBlur(frame_hsv, 5)

            green_extract = cv.inRange(frame_hsv,green_L_hsv,green_U_hsv)
            green_extract = cv.erode(green_extract, None, iterations=2)
            green_extract = cv.dilate(green_extract, None, iterations=2)

            
            possible_balls = cv.HoughCircles(green_extract, cv.HOUGH_GRADIENT, 1, 25, param1=2, param2=20,minRadius=0, maxRadius=0)
            if possible_balls is not None:
                print("Green Ball Found !")
                cv.putText(frame, "Green Ball Detected" ,tuple(map(int,possible_balls[0][0][:2])),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
            else:
                print("Green Ball Not Found !")
                
            """
            ------------Old Code written for SubTask 1-----------------------
            #Boundary/Outline for the Green Ball
            boundary, hierarchy= cv.findContours(green_extract.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
            
            #Contour Area
            if(len(boundary)>0):

                max_contour = max(boundary, key=cv.contourArea)
                ((x, y), radius) = cv.minEnclosingCircle(max_contour )
                points = cv.moments(max_contour)    
                 
                #Finding the center
                center = (int(points['m10'] / points['m00']), int(points['m01'] / points['m00']))
                if radius > 20 :
                    cv.circle(frame, (int(x), int(y)), int(radius),(255, 255, 255), 5)
                    print("FOUND")
                    
                else:
                    print("NOT FOUND")

            cv.imshow("The Actual Frame",frame)
            cv.imshow("Extracted Green ball", green_extract)
            """

            if cv.waitKey(1) & 0xFF == ord('d'):
                break
            ret, jpeg = cv.imencode('.jpg', frame)
            return jpeg.tobytes()

"""
obj = Video()
obj.main_exec()
cv.destroyAllWindows()
"""
