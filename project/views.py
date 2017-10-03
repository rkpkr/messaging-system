from . import app
from flask import render_template, request, flash, redirect
from .forms import Login

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = Login()
	return render_template('login.html',
							form=form)