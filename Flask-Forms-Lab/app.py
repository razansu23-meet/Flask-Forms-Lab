from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = 'kjjnifnqwreuiqgn4jt18518981jr3rj99ht8htu54th88954h54ji4j98j324839tj54'


username = "llo2ay"
password = "123"
facebook_friends=["Sara","Hanan","Marah", "George", "Fouad", "Celina"]


@app.route('/' , methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		user_password = request.form['password']
		if username == name and user_password == password:
			return redirect(url_for('home'))
	return render_template('login.html')

@app.route('/home')  # '/' for the default page
def home():
	return render_template('home.html' , facebook_friends=facebook_friends )
	


@app.route('/friend_exists/<string:name>' ,  methods=['GET', 'POST'])  # '/' for the default page
def friend_exists(name):
	a = False
	if name in facebook_friends:
		a = True
	return render_template('friend_exists.html' , name=name , a = a)
	





if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)