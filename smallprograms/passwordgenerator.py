import re
import random
import string


def passwordcheck(pw):
    if len(pw) < 8:
        point = -1
    elif not re.search("[a-z]", pw):
        point = -1
    elif not re.search("[A-Z]", pw):
        point = -1
    elif not re.search("[0-9]", pw):
        point = -1
    elif not re.search("[_@$&/()=?`%¤#!]", pw):
        point = -1
    else:
        point = 0
        print("Strong Password")
    if point == -1:
        print("Make sure your password contains at least 8 characters, including numbers, symbols and at least one "
              "large character.")


def passwordgenerate(len):
    recipe = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    passw = random.sample(recipe, len)
    password = "".join(passw)
    print(password)


def selection():
    print("Welcome to the strong password assistant. Please choose one of the following options.")

    sel = str(input("1. Check if your password is strong\n2. Create random strong password\n"))

    if sel == "1":
        passwordcheck(str(input("Write your password.\nDisclaimer: It will not be stored anywhere.\n")))

    elif sel == "2":
        len = int(input("How long do you want the password to be?"))
        if len >= 8:
            passwordgenerate(len)
        elif len < 8:
            print("The password should be longer than 8 characters. Try again.")
            selection()


selection()
