import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://www.billboard.com/charts/hot-100"

date = input("Which year do you want to travel to? Type the date in this formate YYYY-MM-DD: ")

response = requests.get(f"{URL}/{date}")
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage,'html.parser')
songs= soup.select(selector='li h3',id='title-of-a-story')
artists = soup.find_all(name="span", class_="u-letter-spacing-0021")
artists_list = []
for artist in artists:
    artists_list.append(artist.getText().strip())
songs_list = []
for song in songs:
    songs_list.append(song.getText().strip())
    if len(songs_list) > 99:
        break


import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify_client_id = "Copy from notes"
spotify_client_secret = "Copy from notes"

sp = spotipy.Spotify(auth_manager=
                    SpotifyOAuth(
                    client_id=spotify_client_id,
                    client_secret=spotify_client_secret,
                    redirect_uri="https://example.org",
                    scope="playlist-modify-private",
                    show_dialog=True,
                    cache_path=".cache",))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
song_uris = []
user_id = sp.current_user()["id"]
print(user_id)
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)