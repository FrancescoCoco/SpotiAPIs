import SpotipyMethod as spMth


def main():
    sp = spMth.authmethod()
    results = spMth.searchmethod(sp, 'cucumba', 20)
    tracks, albums, artists = spMth.trackmethod(sp, results)

    print("TRACKS: ")
    for idx, track in enumerate(tracks):
        print(idx + 1, track.name)
        for artist in track.artists:
            print(artist.name)

    print("\nARTISTS: ")
    for idx, artist in enumerate(artists):
        print(idx + 1, artist.name)

    print("\nALBUM: ")
    for idx, album in enumerate(albums):
        print(idx + 1, album.name)


if __name__ == "__main__":
    main()
