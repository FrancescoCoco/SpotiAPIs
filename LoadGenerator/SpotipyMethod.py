import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Method for authentication
from Artist import Artist


def authmethod():
    # Lines to set the token for spotify developers
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="2b056bd931cf4615967b4897904b99ea",
                                                               client_secret="beacf15fa6744b0ba6e2dd96eb7df10f"))
    return sp

#  Method for search


def searchmethod(sp,searchstr,limit):
    results = sp.search(q=searchstr, limit=limit)
    return results

# Method for track


def trackmethod(results):
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])
        return idx, track

# Method for Artist


def artistmethod(sp,results):
    # list of Artists
    control = False
    artists = []
    for track in (results['tracks']['items']):
        track_artists = track['artists']
        for track_artist in track_artists:
            art = sp.artist(track_artist['id'])
            artist = Artist(art['id'], art['name'], art['followers']['total'], art['genres'], art['popularity'], art['uri'])
            for artist_list in artists:
                if artist_list.id == artist.id:
                    control = True
            if not control:
                artists.append(artist)
            control = False
    return artists

