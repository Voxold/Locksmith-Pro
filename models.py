from config import db
# import bcrypt # bcrypt hash,hashing algorithm used to securely store passwords.


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = password
        # self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        # return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))
        if password == self.password:
            return True
        return False
    
    def __repr__(self,):
        return self.password, self.email, self.name, self.id

class SavedPassword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    password_name = db.Column(db.String(100), nullable=False)
    password_email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    user = db.relationship('User', backref=db.backref('saved_passwords', lazy=True))

    def __repr__(self,):
        return self.password_name, self.password_email, self.password, self.user_id

