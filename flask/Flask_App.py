from flask import Flask,render_template
import Flask_Data as F
import sqlite3
from flask import g




app=Flask(__name__)
app.database="sample.db"

#Routing or mapping. i.e tying a url on wep page to a python function


@app.route('/')
@app.route('/<user>')
def index(user=None):
    g.db=connect_db()
    cur=g.db.execute('select * from posts')
    posts=[dict(title=row[0],description=row[1]) for row in cur.fetchall()]
    g.db.close()
    return  render_template("user.html",user=user,posts=posts)


@app.route('/shopping')
def shopping():
   food=["Cheese","Tuna","Beef","Toothpaste"]
   return render_template("shopping.html",food1=food)    

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html",name=name)     

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good<h2>'


@app.route('/profile1/<username>')
def profile1(username):
    #return "Hey %s"  % username
    return  '<h2>hey {}<h2>'.format(username)


#For non strings data type to be specified between <>
@app.route('/post/<int:post_id>')
def show_post(post_id):
    #return "Hey %s"  % username
    return  '<h2>post_id is {}<h2>'.format(post_id)


def connect_db():
    return sqlite3.connect(app.database)
 
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
