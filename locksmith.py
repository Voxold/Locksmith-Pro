from flask import Flask, request,render_template, redirect,session, jsonify
from config import app, db
from models import User



# Pricipals Pages | DONE
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


# Register Routing ############################## DONE
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

# Login Routing ############################## DONE
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

# Dashboard Routing ############################## DONE
@app.route('/dashboard')
def dashboard():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html',user=user)
    return redirect('/login')

# Logout Routing ############################## DONE
@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/home')

# Check Users in database | DONE
@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users = all_users)


# Dashboard ############################## In Progress
""" !!!! Still Need Modifications !!!!"""

# Save Password
@app.route("/save-password", methods=["POST"])
def save_password():
    name = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")
    type = request.json.get("type")

    if not name or not email:
        return (
            jsonify({"message": "You must be registed"}),
            400,
        )

    new_password = User(name=name, email=email, password=password, type=type)
    try:
        db.session.add(new_password)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Password Saved"}), 201

# Update Password
@app.route("/update_password/<int:user_id>", methods=["PATCH"])
def update_password(user_id):
    myPassword = User.query.get(user_id)

    if not myPassword:
        return jsonify({"message": "Password not found!"}), 404

    data = request.json
    myPassword.name = data.get("Name", myPassword.name)
    myPassword.email = data.get("email", myPassword.email)
    myPassword.email = data.get("password", myPassword.password)

    db.session.commit()

    return jsonify({"message": "Password updated."}), 200

# Delete Password
@app.route("/delete_password/<int:user_id>", methods=["DELETE"])
def delete_password(user_id):
    myPassword = User.query.get(user_id)

    if not myPassword:
        return jsonify({"message": "Password not found"}), 404

    db.session.delete(myPassword)
    db.session.commit()

    return jsonify({"message": "Password deleted!"}), 200



with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)