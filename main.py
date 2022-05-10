from distutils.log import debug
from website import create_app

#Initialize function to return app from init.py
app = create_app()


if __name__ == '__main__':
    app.run(debug=True)