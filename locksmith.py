from flask import Flask, redirect, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def home():
    return render_template('about.html')

@app.route('/contact')
def home():
    return render_template('contact.html')

@app.route('/privacy-policy')
def home():
    return render_template('privacy-policy.html')


if __name__ == '__main__':
    app.run(debug=True)