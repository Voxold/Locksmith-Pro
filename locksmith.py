from flask import Flask, redirect


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1> Hello Locksmith </h1>'