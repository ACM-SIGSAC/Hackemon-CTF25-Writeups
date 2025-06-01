
from flask import Flask, request, session, redirect, url_for, render_template, abort
import secrets
import time

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

tokens = {}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/pre-auth')
def pre_auth():
    token = secrets.token_hex(16)
    tokens[token] = time.time()
    return f"Your pre-auth token: {token}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    token = request.form.get('token')
    if token not in tokens:
        return render_template('error.html', message="Invalid token.")

    if time.time() - tokens[token] > 20:
        return render_template('error.html', message="Token expired.")

    session['logged_in'] = True
    session['visited_race'] = False
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/race')
def race():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    session['visited_race'] = True
    return "You feel like you are on the right track..."

@app.route('/get-flag')
def get_flag():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if not session.get('visited_race'):
        return render_template('error.html', message="You haven't explored enough.")

    return render_template('get_flag.html', flag="ACM{you_found_it}")

@app.route('/fake-flag')
def fake_flag():
    return render_template('fake_flag.html', flag="ACM{this_is_a_trap}")

@app.route('/debug')
def debug():
    abort(403)

@app.errorhandler(403)
def forbidden(e):
    return render_template('error.html', message="Access Denied - You shouldn't be here!"), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/robots.txt')
def robots():
    return "User-agent: *\nDisallow: /race\nDisallow: /debug", 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
