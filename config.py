from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

# Linking Database | DONE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '790b5c87dfc1397fe22e4497bcef23f4'
app.config['WTF_CSRF_ENABLED'] = True

db = SQLAlchemy(app)