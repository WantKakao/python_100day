# 원하는 날짜의 빌보드차트를 내 스포티파이 플레이리스트에 담기
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

url = 'https://www.billboard.com/charts/hot-100/' + date
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

songs = []
for item in soup.select('li.o-chart-results-list__item h3'):
    title = item.get_text(strip=True)
    songs.append(title)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="YOUR_APP_REDIRECTION_URL",
        client_id='YOUR_SPOTIFY_CLIENT_ID',
        client_secret='YOUR_SPOTIFY_CLIENT_SECRET',
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_name = f'{date} Billboard 100'
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description='Billboard Top 100 tracks')

playlist_id = playlist['id']
print(f'Created playlist with ID: {playlist_id}')

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
print('Tracks added to the playlist successfully.')