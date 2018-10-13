from flask import Flask, request, redirect, render_template,logging
import cgi
import os
import jinja2
import string


template_dir = os.path.join (os.path.dirname (__file__), 'templates')
jinja_env = jinja2.Environment (loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route ('/')
def index():
    template = jinja_env.get_template('index.html')
    return template.render()  

def isvalidemail(email):
    if len(email) > 7:
        if email.isspace():
            return True

            if "@" and "." in email:
                return False
            else:
                return True  

def isvalidusername(username):
    username=str(username)
    if username.isspace():
        return True
    else:   
        return False 

@app.route ('/info', methods=['POST'])
def missinginfo():
    username = request.form['username']
    username = str(username)
    username = len(username)
    username_error = " " 

    pword = request.form['pword']
    pword = str(pword)
    pword = len(pword)
    pword_error = " " 

    vpword = request.form['vpword']
    vpword = str(vpword)
    vpword = len(vpword)
    vpword_error = " " 

    email = request.form['email']
    email= str(email)
    email_error = " " 

    app.logger.info("username %s", isvalidusername(username))

    if isvalidusername(username) == True: 
        username_error = "Username cannot include spaces please select a new username"
        username ="" 

    if username > 20 or username < 3: 
        username_error = "Username cannot be empty or less than 4 characters (max 20 characters)"
        username =""   
    
    if pword > 20 or pword < 3: 
        pword_error = "Password cannot be empty or less than 4 characters (max 20 characters)"
        pword = ""   

    if vpword > 20 or vpword < 3: 
        vpword_error = "Verified password cannot be empty or less than 4 characters (max 20 characters)"
        vpword = ""       

    if vpword != pword:
        vpword_error = "Password does not match. Try again."
        vpword =""  

    if isvalidemail(email) == True:
        email_error = "Sorry your did not enter a valid email address please try again."
        email = ""     
        
    if not username_error and not pword_error and not vpword_error and not email_error:
        username = request.form['username']
        return redirect ('/welcome.html'.format(username))
    else: 
        template = jinja_env.get_template('index.html')
        return template.render(username_error=username_error, pword_error=pword_error, vpword_error=vpword_error,email_error=email_error)

@app.route ('/welcome') 
def welcome():
    username=request.form['welcome']
    template = jinja_env.get_template('welcome.html')
    return template.render(username=username)
 

app.run() 