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
import random
import string
import time as t
import MongoLib as ml
import PromLib as prl
import RequestAPIs
import RequestAPIs as rAPIs
import SpotipyMethod as spMth


def main():
    cpu = "0.005"
    mem = "default"

    # Authentication Method with my credentials to spotify for developers
    sp = spMth.authmethod()

    # Start connection with Prometheus
    prom = prl.activate_connection()

    # Connection to the mongodb
    dbmongo = ml.mongo_auth()

    total_albums = None


    """ARTIST"""

    print("Do you want to add artist in SPOTIAPIDB? y or Y for yes ")
    added_artist = input()

    if added_artist == 'y' or added_artist =='Y':
        print("Choose number of artists that you want to add: Minimum(50)")
        number_artist = int(input())
        if number_artist < 50:
            number_artist = 50
        artists_db = spMth.push_item(sp, "artists", number_artist)
        print("Artists founded by spotify, attended to load in the SPOTIAPIDB", len(artists_db))
        rAPIs.post_artists(artists_db)


    total_artists = RequestAPIs.get_all_artists(1)

    # Collects metrics of ENDPOINT RT_FindAllArtists
    if ml.verify_collection(dbmongo, "RT_FindAllArtists", cpu, mem):
        collect_metrics_artist(dbmongo, prom, total_artists, cpu, mem)

    # Collect response times associated with a number of artists required, defined
    print("If you want to collect response times of a particular number of artists digits y or Y ")
    defined_artists = str(input())

    if defined_artists == 'y' or defined_artists == 'Y':
        total_requests = 20
        print("Digit the number of artists  ")
        number_artists = int(input())
        collect_rt_artists_defined(dbmongo, prom, number_artists, total_requests, cpu, mem)


    """ALBUMS"""

    print("Do you want to add album in SPOTIAPIDB? y or Y for yes ")
    added_album = input()

    # Post to insert albums
    if added_album == 'y' or added_album == 'Y':
        print("Choose number of albums that you want to add: Minimum(50)")
        number_albums = int(input())
        if number_albums < 50:
            number_album = 50
        albums_db = spMth.push_item(sp, "albums", number_album)
        print("Albums founded by spotify, attended to load in the SPOTIAPIDB", len(albums_db))
        rAPIs.post_albums(albums_db)

    total_albums = RequestAPIs.get_all_albums(1)

    # Collects metrics of ENDPOINT RT_FindAllAlbums
    if ml.verify_collection(dbmongo, "RT_FindAllAlbums", cpu, mem):
        collect_metrics_albums(dbmongo, prom, total_albums, cpu, mem)

    # Collect response times associated with a number of albums required, defined
    print("If you want to collect response times of a particular number of albums digits y or Y ")
    defined_albums = str(input())
    if defined_albums == 'y' or defined_albums == 'Y':
        total_requests = 10
        print("Digit the number of albums")
        number_albums = int(input())
        collect_rt_albums_defined(dbmongo, prom, number_albums, total_requests, cpu, mem)


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
        t.sleep(1)
        metric_mongo = prl.get_resp_time_findallartist(prom, n_artists, cpu, memory)
        list_metrics_mongo.append(metric_mongo)
        x = x + 1
    random.shuffle(list_metrics_mongo)
    mycol = dbmongo['RT_FindAllArtists']
    mycol.insert_many(list_metrics_mongo)

# Collect response times of defined number of artist in different times
def collect_rt_artists_defined(dbmongo, prom, number_artists, total_request, cpu, memory):
    x = 1
    list_metrics_mongo = []
    while x <= total_request:
        rAPIs.get_all_artists(number_artists)
        t.sleep(1)
        metric_mongo = prl.get_resp_time_findallartist(prom, number_artists, cpu, memory)
        list_metrics_mongo.append(metric_mongo)
        x = x + 1
    mycol = dbmongo['RT_findDefinedArtists' + 'number_artists']
    random.shuffle(list_metrics_mongo)
    mycol.insert_many(list_metrics_mongo)


# Collect metrics album in mongodb
def collect_metrics_albums(dbmongo, prom, total_albums, cpu, memory):
    list_metrics_mongo = []
    list_elements = list([x for x in range(0, total_albums, 40)])
    total_elements = len(list_elements) - 1
    # Artists
    x = 1
    while x <= total_elements:
        n_albums = list_elements[x]
        rAPIs.get_all_albums(n_albums)
        t.sleep(1)
        metric_mongo = prl.get_resp_time_findallalbums(prom, n_albums, cpu, memory)
        list_metrics_mongo.append(metric_mongo)
        x = x + 1
    random.shuffle(list_metrics_mongo)
    mycol = dbmongo['RT_FindAllAlbums']
    mycol.insert_many(list_metrics_mongo)


# Collect response times of defined number of album in different times
def collect_rt_albums_defined(dbmongo, prom, number_albums, total_request, cpu, memory):
    x = 1
    list_metrics_mongo = []
    while x <= total_request:
        rAPIs.get_all_albums(number_albums)
        t.sleep(1)
        metric_mongo = prl.get_resp_time_findallalbums(prom, number_albums, cpu, memory)
        list_metrics_mongo.append(metric_mongo)
        x = x + 1
    mycol = dbmongo['RT_findDefinedAlbums' + 'number_albums']
    random.shuffle(list_metrics_mongo)
    mycol.insert_many(list_metrics_mongo)


if __name__ == "__main__":
    main()
