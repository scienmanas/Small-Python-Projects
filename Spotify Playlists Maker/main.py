from SongList import SongsList, user_input
import spotipy
from spotipy.oauth2 import SpotifyOAuth
Client_ID = "Your Client id"
Client_secret = "Your secret key"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_ID,
        client_secret=Client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="your username"
    )
)
user_id = sp.current_user()["id"]


song_uris = []
year = user_input.split("-")[0]
for song in SongsList:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        
playlist = sp.user_playlist_create(user=user_id, name=f"{user_input} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
