import string
import random

from authlib.common.urls import unquote
from flask import Flask, render_template,session, url_for, redirect, request
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

oauth = OAuth(app)

# TODO: Jak zmienic redirect_uri

spotify = oauth.register(
    name = 'spotify',
    client_id = '64a8ccd2ad2b44b5ad73fcaa7d66db9b',
    client_secret = 'ef2c4f4f51004d40a0042d249ff1de5b',
    authorize_url = 'https://accounts.spotify.com/authorize',
    access_token_url = 'https://accounts.spotify.com/api/token',
    authorize_params = None,
    access_token_params = None,
    userinfo_endpoint='https://api.spotify.com/v1/me',
    client_kwargs={'scope': 'user-read-email user-read-private'},
)

@app.route('/')
def index():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/login')
def login():
    state = ''.join(random.choices(string.ascii_letters + string.digits, k = 16))
    session['state'] = state
    url = url_for('authorize', _external=True)
    return spotify.authorize_redirect(url)

@app.route('/authorize')
def authorize():
    token = spotify.authorize_access_token()
    print(token)
    resp = spotify.get('https://api.spotify.com/v1/me')
    user_info = resp.json()
    session['user'] = user_info
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

