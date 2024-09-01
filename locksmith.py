from flask import Flask, redirect


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1> Hello Locksmith </h1>'


@app.route('/about')
def home():
    return '<h1> Hello Locksmith </h1>'

@app.route('/contact')
def home():
    return '<h1> Contact us </h1>'

@app.route('/privacy')
def home():
    return '<h1> Privacy policy </h1>'


if __name__ == '__main__':
    app.run(debug=True)