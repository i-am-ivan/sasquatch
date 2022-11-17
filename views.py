from flask import Flask
from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/sighting')
def sighting():
    return render_template('edit.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/show')
def show():
    return render_template('show.html')