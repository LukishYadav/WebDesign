from flask import Flask,render_template


app=Flask(__name__)


@app.route('/')
def Hello():
	global x
	x=raw_input("Enter value")


	return render_template('basic.html',var=x)


if __name__=="__main__":
	app.run(debug=True)
