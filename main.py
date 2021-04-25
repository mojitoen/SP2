from flask import *

import passwordgenerator
import re

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
        return f"The URL /passwordgenerator is accessed directly, try going to /tips4 to submit form"
    if request.method == 'POST':
        selection = request.form.get('selection')
        password = request.form.get('password')
        length = request.form.get('length')
        print(selection, password, length)
        if selection == "1":
            strength = passwordgenerator.passwordcheck(password)
            if strength == 0:
                return render_template('passwordgenerator.html', form_data="The password is strong!")
            elif strength == -1:
                return render_template('passwordgenerator.html', form_data="Bad password.. >:(")
            else:
                return render_template('passwordgenerator.html', form_data="Error...")


        elif selection == "2":

            if re.search("[_@$&/()=?`%¤#!]",
                         length):  # Sjekker om det finnes symboler i length, da det vil krasje programmet.
                return render_template('passwordgenerator.html', form_data="You can't use symbols to generate numbers!")

            if length != "":  # Dersom lengden IKKE er tom kjører vi gjennom statementsene under.
                pwlength = int(length)  ## Konverterer til INT

                if pwlength <= 0:
                    return render_template('passwordgenerator.html', form_data="You can't do less than 0!")
                elif pwlength < 8:
                    return render_template('passwordgenerator.html', form_data="The password must be at least 8 "
                                                                               "characters.")
                elif pwlength < 94:  # Sjekker om INT er høyere enn samplinggrensen
                    password = passwordgenerator.passwordgenerate(length)

                    return render_template('passwordgenerator.html', form_data="Your generated password is " + password)

                else:  # Resultatet av if pwlength; dersom det er høyere enn 94 så stopper vi nettsiden fra å krasje.
                    return render_template('passwordgenerator.html', form_data="Too many characters!")
            elif length == "" and password != "":  # Denne sjekker om det er skrevet noe i passordfeltet i stedet for
                # length feltet og forteller at brukeren må fylle inn riktig felt.
                return render_template('passwordgenerator.html', form_data="You must input something!")

        else:  # IKKE RØR DETTE ER CATCH ALLEN FOR DERSOM SELECTION ER NOE ANNET ENN 1 OG 2

            return '<h1> wtf <h1/>'


@app.route('/tips4')
def tips4():
    return render_template('tips4.html')


@app.route('/odin/')
@app.route('/odin/<name>')
def odin(name=None):
    return render_template('odinstest.html', name=name)
