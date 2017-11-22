from flask import Flask,request
import Flask_Data as F

app=Flask(__name__)


#Routing or mapping. i.e tying a url on wep page to a python function


@app.route('/')
def index():
    return 'Method used: %s' % request.method


@app.route('/bacon',methods=['GET','POST'])
def bacon():
    if request.method=='POST':
        return 'You are using POST'
    else:
        return "You are probably using GET"

if __name__=="__main__":
    app.run(debug=True)



#FLASK to Return a CSV response from a dataframe


"""
import pandas as pd
import StringIO
from flask import Flask, Response

data1=pd.read_csv("Output.csv")

@app.route('/some_dataframe.csv')
def output_dataframe_csv():
    
    output = StringIO.StringIO()
    data1.to_csv(output)

    return Response(output.getvalue(), mimetype="text/csv")


if __name__=="__main__":
    app.run(debug=True)"""
