from flask import *

import passwordgenerator

app = Flask(__name__)


# Function index will return the results of render_template('test.html') and will be activated when the index or / is
# seen on the website.
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


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly, try going to /tips3 to submit form"
    if request.method == 'POST':
        form_data = request.form['name']

        return render_template('data.html', form_data=form_data)


@app.route('/passwordgenerator', methods=['POST', 'GET'])
def pwgenerator():
    if request.method == 'GET':
        return f"The URL /passwordgenerator is accessed directly, try going to /passwordgenerator to submit form"
    if request.method == 'POST':
        selection = request.form['selection']
        password = request.form['password']
        length = request.form['length']
        print(selection)
        if selection == "1":
            print("it is going to this one")
            strength = passwordgenerator.passwordcheck(password)
            if strength == 0:
                print("good")
                return f"The password is strong!"
            elif strength == -1:
                print("bad")
                return f"Bad password.. >:("

        elif selection == "2":
            password = passwordgenerator.passwordgenerate(length)
            print(password)
            return password
        else:
            print("wtf")


@app.route('/tips4')
def tips4():
    return render_template('tips4.html')


@app.route('/odin/')
@app.route('/odin/<name>')
def odin(name=None):
    return render_template('odinstest.html', name=name)
