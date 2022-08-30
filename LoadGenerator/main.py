import SpotipyMethod as spMth

def main():
    sp = spMth.authmethod()
    results = spMth.searchmethod(sp,'ozuna',10)
    artists = spMth.artistmethod(sp,results)
    for artist in artists:
        print("Artista: ", artist.name, " Genere:", artist.genres, " Followers: ", artist.followers)


if __name__ == "__main__":
    main()