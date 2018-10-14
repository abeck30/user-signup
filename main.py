from flask import Flask, request, redirect, render_template,logging
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route ('/')
def index():
    template = jinja_env.get_template('index.html')
    return template.render()  

@app.route ('/welcome.html') 
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return template.render(name=username)

@app.route ('/userinfo', methods=['POST'])
def info():
    username = request.form['username']
    pword = request.form['pword']
    vpword = request.form['vpword']
    email = request.form['email']

    username = str(username)
    pword = str(pword)
    vpword = str(vpword)
    email= str(email)

    username_error = " " 
    pword_error = " " 
    vpword_error = " " 
    email_error = " " 

    if len(username) > 20 or len(username) < 3: 
        username_error = "Username cannot be empty or less than 4 characters (max 20 characters)"
        error = username_error
        username =""   
    
    if len(pword) > 20 or len(pword) < 3: 
        pword_error = "Password cannot be empty or less than 4 characters (max 20 characters)"
        error = pword_error
        pword = ""   

    if len(vpword) > 20 or len(vpword) < 3: 
        vpword_error = "Verified password cannot be empty or less than 4 characters (max 20 characters)"
        error = vpword_error
        vpword = ""       

    if vpword != pword:
        vpword_error = "Password does not match. Try again."
        vpword =""  

    if len(email)>0 and len(email)<7:
        email_error = "Sorry your did not enter a valid email address please try again."
        error = email_error
        email = ""     
        
    if not error:
        username = request.form['username']
        return redirect ('/welcome.html')
    else: 
        template = jinja_env.get_template('userinfo.html') 
        return template.render(username_error=username_error, pword_error=pword_error, vpword_error=vpword_error,email_error=email_error)


app.run() 