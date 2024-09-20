from flask import Flask, request, render_template, redirect, jsonify, session, flash

from config import app, db
from models import User
from models import SavedPassword



# Pricipals Pages | DONE
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

# add terms Routing
@app.route('/terms')
def terms():
    return render_template('terms.html', title='Terms of Service')


# Register Routing ############################## DONE
# @app.route('/register',methods=['GET','POST'])
# def register():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
# 
#         new_user = User(name=name,email=email,password=password)
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect('/login')
#     return render_template('register.html')

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Check if the user already exists
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            user_message = "User with this email already exists"
            return render_template('register.html', data=user_message)
        
        # Create a new user
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')
    return render_template('register.html')

# Login Routing ############################## DONE
# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
# 
#         user = User.query.filter_by(email=email).first()
#         
#         if user and user.check_password(password):
#             session['email'] = user.email
#             return redirect('/dashboard')
#         else:
#             return render_template('login.html',error='Invalid user')
#     return render_template('login.html')
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Find the user by email
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            # Set the user session and redirect to dashboard if the password is correct
            session['user_id'] = user.id
            session['email'] = user.email
            session['logged_in'] = True
            return redirect('/dashboard')
        else:
            # Invalid email or password
            return render_template('login.html', error="Invalid email or password")
    return render_template('login.html')


# Dashboard Routing ############################## DONE
# @app.route('/dashboard')
# def dashboard():
#     if session['email']:
#         user = User.query.filter_by(email=session['email']).first()
#         return render_template('dashboard.html',user=user)
#     return redirect('/login')
@app.route("/dashboard")
def dashboard():
    if session['user_id']:
        user_id = session['user_id']
        user = User.query.filter_by(email=session['email']).first()
        # Fetch all saved passwords for the logged-in user
        saves = SavedPassword.query.filter_by(user_id=user_id).all()
        return render_template('dashboard.html', saves=saves, user=user)
    return redirect('/login')

# Logout Routing ############################## DONE
@app.route('/logout')
def logout():
    session.pop('email',None)
    session.pop('logged_in',None)
    return redirect('/home')

# Check Users in database | DONE
@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users = all_users)


# Dashboard Elements ############################## Progrissing

# Save Password | DONE
@app.route("/save", methods=["POST", "GET"])
def save_password():
    if request.method == 'POST':
        # Check if the user is logged in
        if 'user_id' in session:  
            user_id = session['user_id']
            password_name = request.form['name']
            password_email = request.form['email']
            password = request.form['password']

            # Create a new SavedPassword entry
            new_save = SavedPassword(password_name=password_name,
                                     password_email=password_email,
                                     password=password,
                                     user_id=user_id)
            db.session.add(new_save)
            db.session.commit()

            return redirect('/dashboard')
        else:
            return redirect('/login')  # If the user is not logged in, redirect to login
    else:
        return render_template('save.html')

# Update Password | 
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    update = SavedPassword.query.get(id)

    if request.method == 'POST':
        # Handle form data
        update.password_name = request.form.get('name')
        update.password_email = request.form.get('email')
        update.password = request.form.get('password')

        try:
            db.session.commit()
            return redirect('/dashboard')
        except Exception as e:
            return "There was a problem updating the password"
    else:
        return render_template('update.html', update=update)

# Delete Password | DONE
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    myPassword = SavedPassword.query.get(id)
    db.session.delete(myPassword)
    db.session.commit()
    return redirect('/dashboard')

# Delete Users | DONE
@app.route('/delete-user/<int:id>', methods=["POST"])
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect('/users')
    else:
        return "User not found."


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)