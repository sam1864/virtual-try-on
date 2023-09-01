import cvzone
import cv2
from cvzone.PoseModule import PoseDetector
import os
import numpy as np
from django.conf import settings


def video():
    try:

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
    except :
        error=True 
        print("Error occurred.")
        cv2.destroyAllWindows() 
        return error

def specs():
    try:

        cap=cv2.VideoCapture(0)
        detector=PoseDetector()
        sfolder='./static/glass'
        listSpecs=os.listdir(sfolder)
        print(listSpecs)
        fixedratio=188/92
        specsratiowidthheight=392/400
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
                lm2=lmList[2][1:3]
                lm5=lmList[5][1:3]
                lm15=lmList[15][1:3]
                print(lm15)
                imgSpecs=cv2.imread(os.path.join(sfolder,listSpecs[imagenum]),cv2.IMREAD_UNCHANGED)
        
        
                widthofspecs=int((lm2[0]-lm5[0])*fixedratio)
                print(widthofspecs)
                imgSpecs=cv2.resize(imgSpecs,(widthofspecs,int(widthofspecs*specsratiowidthheight)))
                currentscale=(lm2[0]-lm5[0])/92
                offset=int(55*currentscale),int(88*currentscale)   # 43 41
        
                try:

                    img=cvzone.overlayPNG(img,imgSpecs,(lm5[0]-offset[0],lm5[1]-offset[1]))
            
                except:
                    pass
                if lmList[16][1]<150:
                    counterright+=1
                    cv2.ellipse(img,(82, 220),(66,66),0,0,counterright*selectionspeed,(0,255,0),20)
                    if counterright*selectionspeed>360:
                
                        counterright=0
                        if imagenum<len(listSpecs)-1:

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
    except:
        print("Error occurred.")
        error=True
        cv2.destroyAllWindows() 
        return error


def jewellery():
    try:

        cap=cv2.VideoCapture(0)
        detector=PoseDetector()
        sfolder='./static/jew'
        listjews=os.listdir(sfolder)
        print(listjews)
        fixedratio= 182/235  
        jewratiowidthheight=392/400
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
                imgjew=cv2.imread(os.path.join(sfolder,listjews[imagenum]),cv2.IMREAD_UNCHANGED)
        
        
                widthofjews=int((lm11[0]-lm12[0])*fixedratio)
                print(widthofjews)
                imgjew=cv2.resize(imgjew,(widthofjews,int(widthofjews*jewratiowidthheight)))
                currentscale=(lm11[0]-lm12[0])/235
                offset=int(-20*currentscale),int(60*currentscale)     #31 50
        
                try:

                    img=cvzone.overlayPNG(img,imgjew,(lm12[0]-offset[0],lm12[1]-offset[1]))
            
                except:
                    pass
                if lmList[16][1]<150:
                    counterright+=1
                    cv2.ellipse(img,(82, 220),(66,66),0,0,counterright*selectionspeed,(0,255,0),20)
                    if counterright*selectionspeed>360:
                
                        counterright=0
                        if imagenum<len(listjews)-1:

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

    except:
        error=True
        print("Error occurred.")
        cv2.destroyAllWindows() 
        return error
        

   