from dynaconf import FlaskDynaconf
from flask import Flask,render_template
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./templates/index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()