import subprocess

from flask import Flask, render_template, request, session, redirect, url_for

fortune = subprocess.run(['fortune'], stdout=subprocess.PIPE)

@app.route('/fortune/')
def index():
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
