import subprocess

from flask import Flask, render_template, request, session, redirect, url_for

fortune = subprocess.run(['fortune'], stdout=subprocess.PIPE)

@app.route('/fortune/')
def index():
    return fortune


#@app.route('/cowsay/')
#def return stuff

@app.route ('/cowfortune/')
#run fortune, pipe it into cowsay and return it

@app.route('/')
def index():
    return redirect(url_for('fortune'))
