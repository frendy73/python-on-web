from flask import Flask, request, redirect, url_for, render_template, session, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['logged_in'] = True
        return redirect(url_for('dashboard'))
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return 'You are now logged out'

# Status check route
@app.route('/status')
def status():
    if 'logged_in' in session:
        return 'You are currently logged in.'
    else:
        return 'You are NOT logged in.'

@app.route('/dashboard')
@check_logged_in
def dashboard():
    return 'This is the dashboard. You are logged in.'

@app.route('/viewlog')
@check_logged_in
def view_log():
    return 'This is the view log page, accessible only to logged-in users.'

if __name__ == '__main__':
    app.run(debug=True)
