from . import app
from flask import render_template, request, flash, redirect
from .forms import Login

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/login', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		flash('Login requested for {0}'.format(form.user.data))
		return redirect('/main')
	return render_template('login.html',
							form=form)

@app.route('/main', methods=['GET', 'POST'])
def main():
	return render_template('main.html')