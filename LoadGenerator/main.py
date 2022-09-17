import random
import string

import SpotipyMethod as spMth


def main():
    # Authentication Method with my credentials
    sp = spMth.authmethod()

    # SEARCH ARTISTS
    artists_db = spMth.push_item(sp,"artists", 2000)

    # SEARCH ALBUMS
    albums_db = spMth.push_item(sp, "albums", 200)

    # SEARCH TRACKS
    tracks_db = spMth.push_item(sp,"tracks", 200)

    # RESUME
    print("Artisti trovati: ",len(artists_db))
    print("Album trovati: ", len(albums_db))
    print("Canzoni trovate: ", len(tracks_db))

    


if __name__ == "__main__":
    main()
