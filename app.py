#import app1
#print(f"value of __name__ in app.py is : {__name__}")

from flask import Flask,render_template,request#class , function , object and flask->library
import numpy as np
import joblib 

model=joblib.load("knnmodel.pkl")


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('cropform.html')

@app.route('/predict',methods=['GET','POST'])
def prediction():

    testdata=[float(x) for x in request.form.values()]

    print(testdata)

    td=np.array([testdata])

    pred=model.predict(td)

    result=f"Predicted crop is : {pred[0]}"

    return render_template('cropform.html',res=result)

    

if __name__=='__main__':

    app.run(debug=True)