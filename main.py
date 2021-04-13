from flask import *

app = Flask(__name__)

#Function index will return the results of render_template('test.html') and will be activated when the index or / is seen on the website.
@app.route('/')
def Index():
    return render_template('test.html')

@app.route('/tips1')
def tips1():
    return render_template('tips1.html')

@app.route('/tips2')
def tips2():
    return render_template('tips2.html')

@app.route('/tips3')
def tips3():
    return render_template('tips3.html')

@app.route('/tips4')
def tips4():
    return render_template('tips4.html')

@app.route('/odin/')
@app.route('/odin/<name>')
def odin(name=None):
    return render_template('odinstest.html', name=name)
