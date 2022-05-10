#Makes the webiste a python package, so that we can import create_app() in our main.py file

from flask import Flask


def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = 'This is a secret01'
    
    #import views blueprint
    from .views import views

    #Register blueprint
    app.register_blueprint(views, url_prefix = '/')

    return app
