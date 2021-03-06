import cv2 as cv
import numpy as np

class Video (object):
    
    def __init__(self):
        self.camera = cv.VideoCapture(0)
        
    def __del__(self):
        self.camera.release()
        
    def area(self, green_extrac , radius):
        C_x , C_y = (green_extrac.shape[0])/2, (green_extrac.shape[1])/2
        area_covered = str( round( ((3.14159265*pow(radius,2)) * 100 )/(C_x * C_y), 2) )
        return area_covered
    
    def corner(self,green_extrac,x,y):
        C_x , C_y = (green_extrac.shape[0])/2, (green_extrac.shape[1])/2
        if(x < C_x and y < C_y):
            return("Top Left Corner")
        elif(x > C_x and y < C_y):
            return("Top Right Corner")
        elif (x == C_x and y == C_y):
            return ("At the Center")
        elif(x < C_x and y > C_y):
            return("Bottom Left Corner")
        else:
            return("Bottom Right Corner")
        
    def main_exec(self):
        present = False
        area, position = "NULL", "NULL"
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
                present = True
                x,y,radius = map(int,possible_balls[0][0])
                area = self.area(green_extract.copy(), radius)
                position = self.corner(green_extract.copy(), x, y)
                cv.putText(frame, "Green Ball" ,(x,y),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
                cv.circle(frame, (x,y), radius,(80, 255, 255), 2)
                
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
            return jpeg.tobytes(), position, area, present

"""
obj = Video()
obj.main_exec()
cv.destroyAllWindows()
"""
