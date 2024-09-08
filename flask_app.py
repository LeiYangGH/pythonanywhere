
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def index():
    # return 'Hello from Flask github!'
    username = request.form.get('username')
    password = request.form.get('pw')
    return render_template("index.html")

@app.route('/res',methods = ['POST','GET'])
def res():
    username = request.form.get('username')
    password = request.form.get('pw')
    return f"{username} {password}"
