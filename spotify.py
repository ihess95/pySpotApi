import requests

SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/129722926/playlists'
ACCESS_TOKEN = 'BQBr3WCAN0s-FPye3DhHVxhqGgHGY7mzVOd57mT1SPzjgT9nJLXkRwIw7O14KBrFT0saiovGkhJlPHXR5e7TvTZOap7ErlWajqrs9tHZsNdXBEwLxuh87f8AhnwOr-arIPEH-As5as1hxjf_f9ijX-n2CKz1VzC2CIrpnvFqVAoTxcWYZH3NvEgEziIcvd975awIbuOL85b_C7GvofiwzMcQyd6wceKdG7o_j2FGIa0'

def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    response_json = response.json()
    return response_json

def add_song_to_playlist_on_spotify(playlist_id, song_uri):
    response = requests.post(
        f"https://api.spotify.com/v1/playlist/{playlist_id}/tracks?uris={song_uri}",
        headers={"Authorization": f"Bearer {ACCESS_TOKEN}",
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        
        },
    )


def main():
    playlist = create_playlist_on_spotify('test', False)
    song = add_song_to_playlist_on_spotify('1sFHPdJO6X6kfSbA0SKXOe',"spotify%3Atrack%3A5euDb8KdOconOarPzW9pZm")
    
    print(f"Playlist {playlist}")
    print(f"Song {song}")

if __name__ == '__main__':
    main()
