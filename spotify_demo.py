import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up authentication
client_id = 'qwertyu'
client_secret = 'qwertyu'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Example: Search for an artist
artist_name = 'Luke Hemmings'
results = sp.search(q='artist:' + artist_name, type='artist')
items = results['artists']['items']

if len(items) > 0:
    artist = items[0]
    print(f"Name: {artist['name']}")
    print(f"Popularity: {artist['popularity']}")
    print(f"Followers: {artist['followers']['total']}")
    print(artist)
else:
    print(f"No artist found with the name '{artist_name}'")
