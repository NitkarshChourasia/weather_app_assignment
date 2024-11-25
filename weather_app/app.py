from flask import Flask, render_template, request, redirect, session
import json
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "your_secret_key"
bcrypt = Bcrypt(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        with open('data/users.json') as f:
            users = json.load(f)['users']
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and bcrypt.check_password_hash(user['password'], password):
                session['username'] = username
                return redirect('/dashboard')
        return "Invalid credentials"
    return render_template('login.html')