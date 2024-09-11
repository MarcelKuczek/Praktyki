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

@app.route('/playlist')
def get_playlist():
    token = session.get('token', default=None)
    if token is None:
        return redirect(url_for('login'))
    access_token = token['access_token']
    headers = {'Authorization': f'Bearer {access_token}'}
    playlist_response = requests.get('https://api.spotify.com/v1/me/playlists', headers = headers)
    playlist_data = playlist_response.json()
    playlist = playlist_data.get('items', [])
    playlist_name = [playlist.get('name') for playlist in playlist]
    return playlist_name

@app.route('/')
def index():
    token = session.get('token', default=None)
    if token is None:
        return render_template('index.html', user=None)
    access_token = token['access_token']
    headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get('https://api.spotify.com/v1/me', headers = headers)
    playlist = get_playlist()
    user = user_response.json()
    return render_template('index.html', user=user, playlist = playlist)

@app.route('/login')
def login():
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

