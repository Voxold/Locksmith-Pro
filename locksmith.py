from flask import Flask, redirect, render_template, flash, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '790b5c87dfc1397fe22e4497bcef23f4'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact us')

@app.route('/privacy-policy')
def privacy():
    return render_template('privacy-policy.html', title='Privacy policy')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.username.data} !')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form='form')

@app.route('/login')
def login():
    form = LoginForm
    return render_template('login.html', title='Login', form='form')


if __name__ == '__main__':
    app.run(debug=True)