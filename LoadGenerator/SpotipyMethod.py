import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from Artist import Artist
from Album import Album
from Track import Track


# Method for authentication


def authmethod():
    # Lines to set the token for spotify developers
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="2b056bd931cf4615967b4897904b99ea",

                                                               client_secret="beacf15fa6744b0ba6e2dd96eb7df10f"))
    return sp


#  Method for search


def searchmethod(sp, searchstr, limit):
    results = sp.search(q=searchstr, limit=limit)

    return results


# Method for track


def trackmethod(sp, results):
    tracks_founded = []
    albums_founded = []
    artists_founded = []

    control_album = False
    control_artist = False
    control_track = False

    for idx, track_founded in enumerate(results['tracks']['items']):
        album_track = track_founded['album']
        artists_album = album_track['artists']

        #  creation of artists
        artists = []
        for artist_album in artists_album:
            artist = create_artist_album(sp, artist_album)
            artists.append(artist)
            for art in artists_founded:
                if art.name == artist.name:
                    control_artist = True
            if not control_artist:
                artists_founded.append(artist)
            control_artist = False

        #  creation album
        album = creation_album(album_track, artists)

        if album.album_type != 'single':
            for alb in albums_founded:
                if alb.name == album.name:
                    control_album = True
            if not control_album:
                albums_founded.append(album)
            control_album = False

        #  creation of track
        track = creation_track(track_founded, album, artists)

        for trk in tracks_founded:
            if trk.name == track.name:
                control_track = True
        if not control_track:
            tracks_founded.append(track)
        control_track = False

    return tracks_founded, albums_founded, artists_founded


#  Methods for creation


def create_artist_album(sp, artist_album):
    a = sp.artist(artist_album['id'])
    artist = Artist(a['id'], a['name'], a['followers']['total'],
                    a['genres'], a['popularity'], a['uri'])
    return artist


def creation_album(album_track, artists):
    spotify = album_track['external_urls']
    album = Album(album_track['id'],
                  album_track['name'],
                  album_track['release_date'],
                  album_track['album_type'],
                  album_track['total_tracks'],
                  spotify['spotify'],
                  artists)
    return album


def creation_track(track_founded, album, artists):
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
