from flask import Flask, request, redirect
import cgi
import os
import jinja2
import string

template_dir = os.path.join (os.path.dirname (__file__), 'templates')
jinja_env = jinja2.Environment (loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route ('/')
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route ('/missinginfo', methods = ["POST"])
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


    if username > 20 or username < 3: 
        username_error = "Username must be between 4 and 19 characters."
        username =""
    
    if pword > 20 or pword < 3: 
        pword_error = "Password must be between 4 and 19 characters."
        pword = "" 

    if vpword != pword:
        vpword_error = "Password does not match. Try again."
        vpword =""
    
    if not username_error and not pword_error and not vpword_error:
        username = str(username)
        return redirect('/welcome?username={0}'.format(username)) 
    else:
        template = jinja_env.get_template('index.html')
        return template.render(username_error=username_error, pword_error=pword_error, vpword_error=vpword_error)

@app.route('/welcome')
def welcome ():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return template.render(username)
       

app.run() 