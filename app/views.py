from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/officers')
def officers():
    return render_template('officers.html')

@app.route('/programCommittees')
def programCommittees():
    return render_template('programCommittees.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/newsletters')
def newsletters():
    return render_template('newsletters.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
