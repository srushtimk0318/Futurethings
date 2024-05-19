from flask import Flask,render_template,request#'''Flask is framework'''

app=Flask( __name__)

@app.route('/') # '/' is default route and this first to serve whenever it receives request
def index():

    return render_template("fact.html")
    #return "<h1><marquee></marquee><h/1>"#marquee to scroll

@app.route('/findfact',methods=['GET','POST'])
def findfact():

    num=int(request.form['t1'])
    fact=1
    for i in range(1,num+1):
        fact*=i
    
    result=f"Factorial of {num}={fact}"

    return render_template("fact.html",result=result)


app.run(debug=True)#to show result after refresh