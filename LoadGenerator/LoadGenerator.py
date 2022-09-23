"""
██╗░░░░░░█████╗░░█████╗░██████╗
██║░░░░░██╔══██╗██╔══██╗██╔══██╗
██║░░░░░██║░░██║███████║██║░░██║
██║░░░░░██║░░██║██╔══██║██║░░██║╗
███████╗╚█████╔╝██║░░██║██████╔╝
╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
This is main of the Load Generator
"""
import string
import time as t
import MongoLib as ml
import PromLib as prl
import RequestAPIs
import RequestAPIs as rAPIs
import SpotipyMethod as spMth


def main():
    cpu_reserv = "2"
    mem_reserv = "default"

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
        artists_db = spMth.push_item(sp, "artists", 12000)
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

    total_artists = RequestAPIs.get_all_artists(1)

    # Collects metrics of find all artists
    if ml.verify_collection(dbmongo, "RT_FindAllArtists", cpu_reserv, mem_reserv):
        collect_metrics_artist(dbmongo, prom, total_artists, cpu_reserv, mem_reserv)


    # Collect response times associated with a number of artists required, defined
    print("Digita y o Y se vuoi ricalcolare il response time relativo ad un numero di artisti richiesti: ")
    defined_artists = str(input())

    if defined_artists == 'y' or defined_artists == 'Y':
        total_requests = 20
        print("Scrivi il numero di artisti di cui vuoi calcolare il response times: ")
        number_artists = int(input())
        collect_rt_artists_defined(dbmongo, prom, number_artists, total_requests, cpu_reserv, mem_reserv)


# Collect metrics artist in mongodb
def collect_metrics_artist(dbmongo, prom, total_artists, cpu, memory):
    list_metrics_mongo = []
    list_elements = list([x for x in range(0, total_artists, 100)])
    total_elements = len(list_elements) - 1
    # Artists
    x = 1
    while x <= total_elements:
        n_artists = list_elements[x]
        rAPIs.get_all_artists(n_artists)
        t.sleep(2)
        metric_mongo = prl.get_resp_time_findallartist(prom, n_artists, cpu, memory)
        list_metrics_mongo.append(metric_mongo)
        x = x + 1
    mycol = dbmongo['RT_FindAllArtists']
    mycol.insert_many(list_metrics_mongo)


# Collect response times of defined number of artist in different times
def collect_rt_artists_defined(dbmongo, prom, number_artists, total_request, cpu, memory):
    x = 1
    list_metrics_mongo = []
    while x <= total_request:
        rAPIs.get_all_artists(number_artists)
        t.sleep(2)
        metric_mongo = prl.get_resp_time_findallartist(prom, number_artists, cpu, memory)
        list_metrics_mongo.append(metric_mongo)
        x = x + 1
    mycol = dbmongo['RT_findDefinedArtists' + 'number_artists']
    mycol.insert_many(list_metrics_mongo)


if __name__ == "__main__":
    main()
