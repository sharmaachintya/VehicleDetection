import cv2
import imutils

cascade_src='cars.xml'
car_cascade=cv2.CascadeClassifier(cascade_src)
cam=cv2.VideoCapture(0)

while True:
    detected=0
    _,img=cam.read()  #Reading Frame From Camera
    img=imutils.resize(img,width=300)  #Resizing each frame to 300
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Color To Grayscale
    cars=car_cascade.detectMultiScale(gray,1.1,1)  #Coordinates Of Vehicle
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Frame",img)
    detected=int(str(len(cars)))
    print("-----------------------------------------------")
    print("North: %d"%(detected))
    if detected>=2:
        print("North More Traffic")
    else:
        print("No Traffic")
    if cv2.waitKey(33)==27: #Esc to exit
        break
cam.release()
cv2.destroyAllWindows()
