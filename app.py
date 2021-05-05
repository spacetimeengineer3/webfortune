import subprocess
import os
import requests
from flask import Flask, render_template, request, session, redirect, url_for

<<<<<<< HEAD
=======

>>>>>>> 7c57174763159ac69db9c150d0b98e9b54313334
app = Flask(__name__)


@app.route('/fortune/')
<<<<<<< HEAD
def index1():
    fortune = subprocess.run(['fortune'], stdout = subprocess.PIPE)
    message = fortune.stdout.decode()
    return '<pre>' + message + '</pre>'
=======
def fortune():
    fortune = subprocess.run(['fortune'], stdout=subprocess.PIPE)
    fmessage = fortune.stdout.decode()
    return '<pre>' + fmessage + '</pre>'
>>>>>>> 7c57174763159ac69db9c150d0b98e9b54313334


@app.route('/cowsay/')
def cowsay(text):
    cow = subprocess.run(['cowsay', text], stdout=subprocess.PIPE)
    message = cow.stdout.decode()
    return '<pre>' + message + '</pre>'

@app.route ('/cowfortune/<text>/')
def cowfortune():
    fortune = subprocess.run(['fortune'],stdout=subprocess.PIPE)
    fmessage = fortune.stdout.decode()
    
    cow = subprocess.run(['cowsay', fmessage], stdout=subprocess.PIPE)
    cmessage = cow.stdout.decode()

    return '<pre>' + cmessage + '</pre>'


@app.route('/')
def index():
    return redirect(url_for('fortune'))
