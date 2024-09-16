from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Linking Database | DONE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '790b5c87dfc1397fe22e4497bcef23f4'
db = SQLAlchemy(app)