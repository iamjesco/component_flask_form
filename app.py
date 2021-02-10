from flask import Flask, render_template, redirect, url_for, request, session, g, flash
from forms.forms import SignUp, Login
from models.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'srgsRFGTAEWRgQgeqwe'

users = [
	{
		'username': 'jurgens',
		'password': 'test',
		'email': 'jurgen.schoobaar@pinnacle.com'
	}
]


@app.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		for user in users:
			if user['username'] == session['user_id']:
				g.user = user


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
			request.form.get('password'),
		)
		print(username)
		return redirect(url_for('success'))
	return render_template('signup.html', form=form)


@app.route('/blog')
def blog():
	if not g.user:
		# abort(403)
		return redirect(url_for('login'))
	return render_template('blog.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
	form = Login()
	if form.validate_on_submit():
		session.pop('user_id', None)
		username = form.username.data
		password = form.password.data
		for user in users:
			if username == user['username'] and password == user['password']:
				session['user_id'] = user['username']
				return redirect(url_for('home'))
			flash('username and password do not match!')
			return redirect(url_for('login'))
	return render_template('login.html', form=form)


@app.route('/sign-out')
def sign_out():
	session.pop('user_id')
	return redirect(url_for('home'))


@app.route('/success')
def success():
	return render_template('success.html')


if __name__ == '__main__':
	app.run(debug=True)
