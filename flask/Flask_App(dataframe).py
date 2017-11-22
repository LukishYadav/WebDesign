from flask import Flask
import Flask_Data as F
import pandas as pd
import StringIO
from flask import Flask, Response

app=Flask(__name__)

#FLASK to Return a CSV response from a dataframe





data1=pd.read_csv("Output.csv")

@app.route('/output.csv')
def output_dataframe_csv():
    
    output = StringIO.StringIO()
    data1.to_csv(output)
    #return 'test'
    return Response(output.getvalue(), mimetype="text/csv")


if __name__=="__main__":
    app.run(debug=True)
