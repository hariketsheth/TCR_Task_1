import cv2 as cv

class Video:
    
    def __init__(self):
        self.camera = cv.VideoCapture(0)

    def __del__(self):
        self.camera.release()
 
    def main_exec(self):
        green_L_hsv = (36, 86, 6)
        green_U_hsv = (86, 255, 255)
        while True:
            response, frame = self.camera.read()
            if frame is None:
                break

            frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

            green_extract = cv.inRange(frame_hsv,green_L_hsv,green_U_hsv)
            green_extract = cv.erode(green_extract, None, iterations=2)
            green_extract = cv.dilate(green_extract, None, iterations=2)

            #Boundary/Outline for the Green Ball
            boundary, hierarchy= cv.findContours(green_extract.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
            
            #Contour Area
            if(len(boundary)>0):

                max_contour = max(boundary, key=cv.contourArea)
                ((x, y), radius) = cv.minEnclosingCircle(max_contour )
                points = cv.moments(max_contour)            
                
            if green_extract is not None:
                print("FOUND")

            cv.imshow("window1",frame)
            cv.imshow("window2", green_extract)

            if cv.waitKey(1) & 0xFF == ord('d'):
                break

obj = Video()
obj.main_exec()
cv.destroyAllWindows()
