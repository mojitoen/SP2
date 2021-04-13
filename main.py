from flask import *

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def Index(name=None):
    return render_template('test.html', name=name)

@app.route('/odin/')
@app.route('/odin/<name>')
def odin(name=None):
    return render_template('odinstest.html', name=name)