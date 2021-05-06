import subprocess
import os
import requests
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)


@app.route('/fortune/')
def index1():
    fortune = subprocess.run(['fortune'], stdout = subprocess.PIPE)
    message = fortune.stdout.decode()
    return '<pre>' + message + '</pre>'
def fortune():
    fortune = subprocess.run(['fortune'], stdout=subprocess.PIPE)
    fmessage = fortune.stdout.decode()
    return '<pre>' + fmessage + '</pre>'


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
    return redirect(url_for('/fortune/'))
