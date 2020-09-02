from flask import flask, render template

app=flask (__name__)

@app.route('/')
def index ( ):
name = "swan"
return render template('index.html',name=name)
