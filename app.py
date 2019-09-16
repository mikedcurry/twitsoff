"""Main Application and routing Logic for Twitsoff"""
from flask import Flask

def create_app():
    """create and config an instance of the Flask App"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Welcome to Twitsoff'

    return app