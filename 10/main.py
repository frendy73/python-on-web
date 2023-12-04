from flask import Flask, request, render_template_string, redirect, url_for, session
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'

search_log = []

@app.route('/')
def home():
    return render_template_string('''
        <html>
            <head>
                <title>Search4Letters</title>
            </head>
            <body>
                <h1>Welcome to search4letters on the web!</h1>
                <form method="post" action="/search">
                    Phrase: <input type="text" name="phrase"><br>
                    Letters: <input type="text" name="letters"><br>
                    <input type="submit" value="Do it!">
                </form>
            </body>
        </html>
    ''')

@app.route('/search', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = set(re.findall('[' + letters + ']', phrase))
    search_log.append((phrase, letters, request.remote_addr, request.user_agent.browser, str(results)))
    return render_template_string('''
        <html>
            <head>
                <title>Search Results</title>
            </head>
            <body>
                <h1>{{ title }}</h1>
                <p>You searched for: {{ phrase }}<br>
                Using the letters: {{ letters }}<br>
                Results: {{ results }}</p>
                <a href="/">Try again</a>
            </body>
        </html>
    ''', phrase=phrase, letters=letters, title=title, results=results)

@app.route('/viewlog')
def view_the_log():
    if 'logged_in' in session:
        return render_template_string('''
            <html>
                <head>
                    <title>View Log</title>
                </head>
                <body>
                    <h1>View Log</h1>
                    <table>
                        <tr><th>Phrase</th><th>Letters</th><th>Remote_addr</th><th>User_agent</th><th>Results</th></tr>
                        {% for row in log %}
                        <tr><td>{{ row[0] }}</td><td>{{ row[1] }}</td><td>{{ row[2] }}</td><td>{{ row[3] }}</td><td>{{ row[4] }}</td></tr>
                        {% endfor %}
                    </table>
                </body>
            </html>
        ''', log=search_log)
    else:
        return 'You are NOT logged in.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['logged_in'] = True
        return redirect(url_for('home'))
    return '<form method="post">Click to log in: <button type="submit">Login</button></form>'

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
