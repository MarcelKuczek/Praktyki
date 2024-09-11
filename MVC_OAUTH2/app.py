import string
import random
from os import access
from authlib.common.urls import unquote
from flask import Flask, render_template,session, url_for, redirect
import requests
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
    userplaylist_endpoint = 'https://api.spotify.com/v1/me/playlists',
    client_kwargs={'scope': 'user-read-email user-read-private'},
)

@app.route('/')
def index():
    token = session.get('token')
    access_token = 'Your_access_token'
    url = 'https://api.spotify.com/v1/me'
    headers = {
        'Autorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers = headers)
    print(response)
    token = session.get('token', default=None)
    print(f"Token: {token}")
    if token is None:
        user = session.get('user')
        return render_template('index.html', user=user)

    access_token = token['access_token']
    print (access_token)
    #user = requests.get('', headers={ 'Authorization': 'Bearer {token}' } ) json
    return render_template('index.html', user=None)

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
    session['token'] = token
    resp = spotify.get('https://api.spotify.com/v1/me')
    user_info = resp.json()
    session['user'] = user_info
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('token', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

