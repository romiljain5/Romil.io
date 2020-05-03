from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '6a6eb64eb5cb63a407685a4f06b233ff'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# ======== for resetting database remove below two ===========
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
# ---------- for sending mails email ---------- #
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
    # mail and password
    
from pain.models import EmailNPss
app.config['MAIL_USERNAME'] = "yourEmail" #k.username12
app.config['MAIL_PASSWORD'] = "yourPassword" #k.password12
mail = Mail(app)

from pain import routes