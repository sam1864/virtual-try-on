import cvzone
import cv2
from cvzone.PoseModule import PoseDetector
import os
import numpy as np
from django.conf import settings


def video():
    cap=cv2.VideoCapture(0)
    detector=PoseDetector()
    sfolder = './static/shirts' 
    listShirts=os.listdir(sfolder)
    print(listShirts)
    fixedratio=474/353 
    shirtratiowidthheight=392/400
    imagenum=0
    #imgbutton=cv2.imread("./buttons/right.png",cv2.IMREAD_UNCHANGED)
    counterleft=0
    counterright=0
    selectionspeed=10

    while True:
        success,img=cap.read()
        img=detector.findPose(img)
    #img=cv2.flip(img,1)
        lmList,bboxInfo=detector.findPosition(img,bboxWithHands=False,draw=False)
        if lmList:
            lm11=lmList[11][1:3]
            lm12=lmList[12][1:3]
            lm15=lmList[15][1:3]
            print(lm15)
            imgShirt=cv2.imread(os.path.join(sfolder,listShirts[imagenum]),cv2.IMREAD_UNCHANGED)
        
        
            widthofshirts=int((lm11[0]-lm12[0])*fixedratio)
            print(widthofshirts)
            imgShirt=cv2.resize(imgShirt,(widthofshirts,int(widthofshirts*shirtratiowidthheight)))
            currentscale=(lm11[0]-lm12[0])/353
            offset=int(77*currentscale),int(54*currentscale)
        
            try:

                img=cvzone.overlayPNG(img,imgShirt,(lm12[0]-offset[0],lm12[1]-offset[1]))
            
            except:
                pass
            if lmList[16][1]<150:
                counterright+=1
                cv2.ellipse(img,(82, 220),(66,66),0,0,counterright*selectionspeed,(0,255,0),20)
                if counterright*selectionspeed>360:
                
                    counterright=0
                    if imagenum<len(listShirts)-1:

                        imagenum+=1

                  
            elif lmList[15][1]>=556:
                counterleft+=1
                cv2.ellipse(img,(556, 220),(66,66),0,0,counterleft*selectionspeed,(0,255,0),20)
                if counterleft*selectionspeed>360:
                
                    counterleft=0
                    if imagenum>0:

                        imagenum-=1


            
            else:
                counterright=0
                counterleft=0

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break



       
        
        cv2.imshow("Image",img)
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    cap.release()

