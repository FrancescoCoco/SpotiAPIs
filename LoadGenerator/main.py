import time as t
import MongoLib as ml
import PromLib as prl
import RequestAPIs
import RequestAPIs as rAPIs
import SpotipyMethod as spMth

def main():
    # Authentication Method with my credentials to spotify for developers
    sp = spMth.authmethod()

    # Start connection with Prometheus
    prom = prl.activate_connection()

    # Connection to the mongodb
    dbmongo = ml.mongo_auth()

    total_artists = RequestAPIs.get_all_artists(1)
    total_albums = None
    total_tracks = None

    # Post to insert artist
    if total_artists == 0:
        artists_db = spMth.push_item(sp, "artists", 2000)
        print("Artisti trovati da Spotify in attesa di caricamento tramite il microservizio: ", len(artists_db))
        rAPIs.post_artists(artists_db)

    # Post to insert albums
    if total_albums is not None:
        albums_db = spMth.push_item(sp, "albums", 200)
        print("Album trovati da Spotify in attesa di caricamento tramite il microservizio: ", len(albums_db))
        rAPIs.post_albums(albums_db)

    # Post to insert tracks
    if total_tracks is not None:
        tracks_db = spMth.push_item(sp, "tracks", 10)
        print("Canzoni trovate: ", len(tracks_db))

    # Collects metrics of find all artists
    if ml.verify_collection(dbmongo, "RT_FindAllArtists"):
        collect_metrics_artist(dbmongo, prom, total_artists)


# Collect metrics artist in mongodb
def collect_metrics_artist(dbmongo, prom, total_artists):
    list_metrics_mongo = []
    list_elements = list([x for x in range(0, total_artists, 100)])
    total_elements = len(list_elements) - 1
    # Artists
    x = 1
    while x <= total_elements:
        t.sleep(1)
        n_artists = list_elements[x]
        print(n_artists)
        rAPIs.get_all_artists(n_artists)
        t.sleep(1)
        metric_mongo = prl.get_resp_time_findallartist(prom, n_artists, 'default', 'default')
        list_metrics_mongo.append(metric_mongo)
        x = x + 1
    mycol = dbmongo['RT_FindAllArtists']
    mycol.insert_many(list_metrics_mongo)


if __name__ == "__main__":
    main()
