import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

client_id = '5f42272777a54dd99bb971efee6c6c55'
client_secret = '1c6286ef55df483786ca8fef0f25e092'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


