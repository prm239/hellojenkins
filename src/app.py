from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
	return "Hello Jenkins*****8\n"
app.run(host="0.0.0.0",port="5000")
