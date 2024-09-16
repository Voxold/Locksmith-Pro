from flask import Flask, request,render_template, redirect,session
from flask_sqlalchemy import SQLAlchemy
import bcrypt # bcrypt hash,hashing algorithm used to securely store passwords.


app = Flask(__name__)
# Linking Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '790b5c87dfc1397fe22e4497bcef23f4'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', )


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact us')

@app.route('/privacy-policy')
def privacy():
    return render_template('privacy-policy.html', title='Privacy policy')

# add terms Routing
@app.route('/terms')
def terms():
    return render_template('terms.html', title='Terms of Service')


# Register Routing ##############################
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

# Login Routing ##############################
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html',error='Invalid user')
    return render_template('login.html')

# Dashboard Routing ##############################
@app.route('/dashboard')
def dashboard():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html',user=user)
    return redirect('/login')

# Logout Routing ##############################
@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/home')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()

# To See Who Users in database
@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users = all_users)


if __name__ == '__main__':
    app.run(debug=True)