"""Main Application and routing Logic for Twitsoff"""
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

def create_app():
    """create and config an instance of the Flask App"""
    app = Flask(__name__)

    #add config here later:
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    # Stop tracking modifications
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['ENV'] = config('ENV')

    #now the database knows about the app
    DB.init_app(app)

    # Create route
    @app.route('/')
    def root():
        users = Users.query.all()
        return render_template('base.html', title = 'Home', users=users)

    return app