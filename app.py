import subprocess
import os
from flask import Flask, render_template, request, session, redirect, url_for

fortune = subprocess.run(['fortune'], stdout=subprocess.PIPE)

app = Flask(__name__)
#app.secret_key = b'REPLACE_ME_x#pi*CO0@^z'


@app.route('/fortune/')
def index1():
    return fortune


@app.route('/cowsay/')
def cowsay(text):
    cow = subprocess.run(['cowsay', text], stdout=subprocess.PIPE)
    message = cow.stdout.decode()
    return '<pre>' + message + '</pre>'

@app.route ('/cowfortune/')
def cowfortune():
    fortune = subprocess.run(['fortune'],stdout=subprocess.PIPE)
    fmessage = fortune.stdout.decode()
    
    cow = subprocess.run(['cowsay', fmessage], stdout=subprocess.PIPE)
    cmessage = cow.stdout.decode()

    return '<pre>' + cmessage + '</pre>'


@app.route('/')
def index():
    return redirect(url_for('fortune'))
