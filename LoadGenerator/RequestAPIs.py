"""
██████╗░███████╗░██████╗░██╗░░░██╗███████╗░██████╗████████╗░█████╗░██████╗░██╗░██████╗
██╔══██╗██╔════╝██╔═══██╗██║░░░██║██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║██╔════╝
██████╔╝█████╗░░██║██╗██║██║░░░██║█████╗░░╚█████╗░░░░██║░░░███████║██████╔╝██║╚█████╗░
██╔══██╗██╔══╝░░╚██████╔╝██║░░░██║██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║██╔═══╝░██║░╚═══██╗
██║░░██║███████╗░╚═██╔═╝░╚██████╔╝███████╗██████╔╝░░░██║░░░██║░░██║██║░░░░░██║██████╔╝
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░
"""

import json
import requests


def post_artists(artists):
    url_post_artist = "http://localhost:8080/artist/addartist"
    for artist in artists:
        try:
            data_artist = artist.to_dict()
            response = requests.post(url_post_artist, json=data_artist)
            print("JSON RESPONSE", response.json())
        except json.decoder.JSONDecodeError:
            pass



def get_all_artists(value: int):
    url_find_all_artists = "http://localhost:8080/artist/findallartists/" + str(value)
    try:
        response = requests.get(url_find_all_artists)
        total_elements = int(response.json()['totalElements'])
    except json.decoder.JSONDecodeError:
        total_elements = 0
        pass
    return total_elements


def post_albums(albums):
    url_post_album = "http://localhost:8080/album/addalbum"
    for album in albums:
        try:
            data_album = album.to_dict()
            response = requests.post(url_post_album, json= data_album)
            print("JSON RESPONSE", response.json())
        except json.decoder.JSONDecodeError:
            pass


def post_tracks(tracks):
    data = [track.to_dict() for track in tracks]
    print(data)

