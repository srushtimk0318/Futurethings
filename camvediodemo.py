import cv2 
import random


cam=cv2.VideoCapture(0)#computer vision-> cv2 , 

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#cascadeclass->algorithm to load model, haar-> model 

while True:
    flag,image=cam.read()#flag->variable takes boolean values , image -> obj
    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#cvtcolor    -> object to convert color
    
    faces=cascade.detectMultiScale(gray_image,1.1,5)#1.1,5->hyperparameters helps to tune the object , detectmultiscale-> returns a list of rectangles of all the detected objects

    if len(faces)>0:
        x,y,w,h=faces[0]#[0]-> first person store using x,y,w,h
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,100,0),2)#gbr->255,200,  2->thickness
        
        
    #for x,y,w,h in faces:
    
      # cv2.rectangle(image,(x,y),(x+w,y+h),(255,100,0),2)

    print(faces)

    cv2.imshow("Myimage",image)
    k=cv2.waitKey(2)#showing image 2 miliseconds and info abt which key we press
    
    if k==ord('q'):#ASIC no. of q is defined by org(library)
        break

    if k==ord('s'): 
        cropped=image[y:y+h,x:x+w]#width an dheight
        cropped=cv2.resize(cropped,(300,300))
        index=random.randint(0,100)#random number for names of saved image
        path=f"dataset/3/person{index}.jpg"
        cv2.imwrite(path,cropped)#imwrite saves image


    '''gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("My_Gray_image",gray_image)
    cv2.waitKey()'''
  

cam.release()