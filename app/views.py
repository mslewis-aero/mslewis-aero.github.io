from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/officers')
def officers():
    return render_template('officers.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html',calendar=True)

@app.route('/newsletters')
def newsletters():
    return render_template('newsletters.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s'
               %(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')

    return render_template('login.html',
                           title='Sign In',
                           form=form)
