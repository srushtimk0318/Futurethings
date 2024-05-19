from os import listdir
import cv2
import numpy as np

root_dir="./dataset"

features=[]#empty list to store
labels=[]
l=0
for folder in listdir(root_dir):
    print(f"-----files in the folder {folder} are  ---------")
    
    path=f"{root_dir}/{folder}"
    
    for file in listdir(path):
        filepath=f"{path}/{file}"
        
        image=cv2.imread(filepath,0)
        cv2.imshow("demo",image)
        cv2.waitKey()
        
        # print(image)
        features.append(image)
        labels.append(l) 
    l=l+1#increment sub-folder


print(f"features are...{features}") 
print(f"Labels are {labels}")

print(f"{len(features)},{len(labels)}")

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(features,np.array(labels))

#Here we are training the machine using LBPH

recognizer.save("facemodel.yml")

#Above statement exports trained model to external file
