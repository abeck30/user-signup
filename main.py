from flask import Flask, request, redirect, render_template
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index ():
    return render_template("userinfo.html")

@app.route('/signup', methods=['POST'])
def validate_userinfo():
    username = request.form['form_name']
    password = request.form ['pass_word']
    vpassword = request.form['vp_word']
    useremail = request.form['useremail']

    form_name_error = " "
    pass_word_error = " "
    vp_word_error = " "
    useremail_error = " "
   

    if len(username) > 20 or len(username) < 3:
        form_name_error = "Username must be greater than 3 characters and less than 20 characters"
        username = ''
    elif " " in username:
        form_name_error = "Username cannot contain spaces"
        username = ''

    if len(password) > 20 or len(password) < 3:
        pass_word_error = "Password must be longer than 3 characters and less than 20 "
        password = ''
    elif " " in password:
        pass_word_error = "Password connot contain spaces "
        password = ''
    
    if len(vpassword) > 20 or len(vpassword) < 3:
        vp_word_error = "Password must be longer than 3 characters and less than 20"
        vpassword = ''
    elif vpassword != password:
        vp_word_error = "Password verification does not match Password"
        vpassword = ''

    if len(useremail) > 0  and len(username) < 7:
        useremail_error = "Not a valid email" 
        useremail = ''   
        if " " in useremail:
            useremail_error = "Not a valid email" 
            useremail = ''
        elif "@" and "." not in useremail:
            useremail_error = "Not a valid email" 
            useremail = '' 

       
    if not form_name_error and not pass_word_error and not vp_word_error and not useremail_error:
        return render_template('userwelcome.html', username=username )
    else:
        return render_template('userinfo.html', form_name_error=form_name_error, pass_word_error=pass_word_error, vp_word_error=vp_word_error, useremail_error=useremail_error, username=username, password=password,vpword=vpassword,useremail=useremail)   

app.run()