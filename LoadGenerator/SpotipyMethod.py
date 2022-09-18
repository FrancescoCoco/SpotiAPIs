import random
import string

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from Artist import Artist
from Album import Album
from Genre import Genre
from Track import Track


# Method for authentication
def authmethod():
    # Lines to set the token for spotify developers
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="2b056bd931cf4615967b4897904b99ea",
                                                               client_secret="beacf15fa6744b0ba6e2dd96eb7df10f"))
    return sp


# METHODS FOR SEARCH

# Method for search artists
def search_artists(sp, searchstr, limit):
    results = sp.search(q=searchstr, limit=limit, type="artist")
    artists = []
    artists_founded = results['artists']['items']
    for artist_founded in artists_founded:
        artist = model_artist(sp, artist_founded)
        artists.append(artist)
    return artists


# Method for search albums
def search_albums(sp, searchstr, limit):
    results = sp.search(q=searchstr, limit=limit, type="album")
    albums = []
    albums_founded = results['albums']['items']
    for album_founded in albums_founded:
        artists_album_founded = []
        artists_album = album_founded['artists']
        for artist_album in artists_album:
            artist = model_artist_album(sp, artist_album)
            artists_album_founded.append(artist)
        album = model_album(album_founded, artists_album_founded)
        albums.append(album)
    return albums


# Method for search track
def search_tracks(sp, searchstr, limit):
    tracks = []
    results = sp.search(q=searchstr, limit=limit, type="track")
    tracks_founded = results['tracks']['items']
    for track_founded in tracks_founded:
        album_track = track_founded['album']
        artists_album = album_track['artists']
        artists = []
        for artist_album in artists_album:
            artist = model_artist_album(sp, artist_album)
            artists.append(artist)
        #  creation album
        album = model_album(album_track, artists)
        #  creation of track
        track = model_track(track_founded, album, artists)
        tracks.append(track)
    return tracks


#  MODELING

# Model artist of an album
def model_artist_album(sp, artist_album):
    a = sp.artist(artist_album['id'])
    genres = model_genres(a['genres'])
    artist = Artist(a['id'], a['name'], a['followers']['total'],
                    genres, a['popularity'], a['uri'])
    return artist


# Model genres:
def model_genres(genres):
    genres_found = []
    for genre in genres:
        genre_found = Genre(genre)
        genres_found.append(genre_found)
    return genres_found


#  Model artist
def model_artist(sp, artist):
    a = artist
    genres = model_genres(a['genres'])
    artist = Artist(a['id'], a['name'], a['followers']['total'],
                    genres, a['popularity'], a['uri'])
    return artist


#  Model album
def model_album(album, artists):
    spotify = album['external_urls']
    album = Album(album['id'],
                  album['name'],
                  album['release_date'],
                  album['album_type'],
                  album['total_tracks'],
                  spotify['spotify'],
                  artists)
    return album


#  Model tracks
def model_track(track_founded, album, artists):
    spotify = track_founded['external_urls']
    release_data = album.release_date
    track = Track(track_founded['id'],
                  track_founded['name'],
                  track_founded['duration_ms'],
                  release_data,
                  spotify['spotify'],
                  album,
                  artists
                  )

    return track


def control_itemdb(item, items_db):
    control = False
    for item_db in items_db:
        if item_db.name == item.name or item_db.id == item.id:
            control = True
    if not control:
        items_db.append(item)
    return items_db


# PUSH ITEMS ON DB
def push_item(sp, type_item, value_search):
    lower_upper_alphabet = string.ascii_letters
    items_db = []
    while len(items_db) < value_search:
        random_letters = random.choice(lower_upper_alphabet) + random.choice(lower_upper_alphabet) \
                         + random.choice(lower_upper_alphabet)
        # SEARCH ARTISTS
        if type_item == 'artists':
            artists = search_artists(sp, random_letters, 50)
            for idx, artist in enumerate(artists):
                items_db = control_itemdb(artist, items_db)
        # SEARCH ALBUMS
        if type_item == 'albums':
            albums = search_albums(sp, random_letters, 50)
            print("\nALBUM: ")
            for idx, album in enumerate(albums):
                items_db = control_itemdb(album, items_db)
        # SEARCH TRACKS
        if type_item == 'tracks':
            tracks = search_tracks(sp, random_letters, 50)
            print("\nTRACKS: ")
            for idx, track in enumerate(tracks):
                items_db = control_itemdb(track, items_db)

        print(len(items_db))

    return items_db
