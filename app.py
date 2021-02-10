from flask import Flask, render_template, redirect, url_for, request
from forms.signup import SignUp
from models.users import User

app = Flask(__name__)
app.secret_key = 'qwregw346tq3wrgeqw456tqt4q'


@app.route('/')
def index():
	return redirect(url_for('home'))


@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/signup', methods=('GET', 'POST'))
def signup():
	form = SignUp()
	if form.validate_on_submit():
		username = User(
			request.form.get('username'),
			request.form.get('email'),
			request.form.get('password')
		)
		print(username)
		return redirect(url_for('success'))
	return render_template('signup.html', form=form)


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/success')
def success():
	return render_template('success.html')


if __name__ == '__main__':
	app.run(debug=True)
