import requests
apikey="2bd7c775ee9ce7b80a2712abcdd5361b"
import joblib
import numpy as np


def fetch_weather(cityname):
    
    url=f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apikey}"
    
    
    response=requests.get(url)#get -> show the result just like enter

    print(response)

    if response.status_code==200:
        
        print("Done successfull")
        
        # print( response.json() )
        
        result=response.json()#json-> used to #convert web response to python dictionary form
        
        x=result['main']
        
        temp=x['temp']-273.15
        pressure=x['pressure']
        humidity=x['humidity']

        model=joblib.load("knncropmodel.pkl")#knncropmodel-> algorithm load by calling joblib

        testdata=np.array([[temp,humidity]])
        pred=model.predict(testdata)
        
        msg=f"Weahter info is..\ntemp:{temp} degree cel\nPressure : {pressure}\nHumidity : {humidity}\nRecomended crop is : {pred[0]}"
        
        
        

    else:
        msg="Some thing went wrong !"
    
    
    return msg   
