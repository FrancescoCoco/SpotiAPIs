"""
░██████╗███████╗███╗░░██╗░██████╗██╗████████╗██╗██╗░░░██╗███████╗
██╔════╝██╔════╝████╗░██║██╔════╝██║╚══██╔══╝██║██║░░░██║██╔════╝
╚█████╗░█████╗░░██╔██╗██║╚█████╗░██║░░░██║░░░██║╚██╗░██╔╝█████╗░░
░╚═══██╗██╔══╝░░██║╚████║░╚═══██╗██║░░░██║░░░██║░╚████╔╝░██╔══╝░░
██████╔╝███████╗██║░╚███║██████╔╝██║░░░██║░░░██║░░╚██╔╝░░███████╗
╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝

░█████╗░███╗░░██╗░█████╗░██╗░░░░░██╗░░░██╗███████╗███████╗██████╗░
██╔══██╗████╗░██║██╔══██╗██║░░░░░╚██╗░██╔╝╚════██║██╔════╝██╔══██╗
███████║██╔██╗██║███████║██║░░░░░░╚████╔╝░░░███╔═╝█████╗░░██████╔╝
██╔══██║██║╚████║██╔══██║██║░░░░░░░╚██╔╝░░██╔══╝░░██╔══╝░░██╔══██╗
██║░░██║██║░╚███║██║░░██║███████╗░░░██║░░░███████╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝

This is main of the Load Generator
"""

import random
import MongoLib as ml
from RegressionLib import scatterplot_model, linear_regression, polynomial_regression, hist_rt_nartists


def main():
    cpu = "2"
    memory = "default"

    # Connection to the mongodb
    dbmongo = ml.mongo_auth()

    # Catch dataset
    response_times, number_artist = catch_rt_artist(dbmongo, 'RT_FindAllArtists', cpu, memory)

    # plot original model
    scatterplot_model(number_artist, response_times, "Model\nEndpoint: findallartists"
                      + "\nCPU: " + cpu + "\nMemory:" + memory,
                      "number artists", "response time(ms)")

    # linear regression
    linear_regression(number_artist, response_times, "Linear Regression\nEndpoint: findallartists"
                      + "\nCPU: " + cpu + "\nMemory:" + memory, "number artists", "response time(ms)")

    # polynomial regression
    degree = 3 # parameter to express the degree of polynomial regression
    polynomial_regression(number_artist, response_times, "Polynomial Regression\nEndpoint: findallartists"
                          + "\nCPU: " + cpu + "\nMemory:" + memory, "number artists", "response time(ms)",3)

    # Question if you want to plot  response times associated with a number of artists defined
    print("Scrivi y se vuoi plottare l'istogramma dei response times calcolati su un numero di artisti definiti ")
    defined_artists = str(input())

    if defined_artists == 'y':
        print("Scrivi il numero di artisti di cui vuoi plottare il response times: ")
        number_artists = int(input())
        # Fetch response times associated with a number of artists required, defined
        response_times_art_def, number_artist_def = catch_response_times_by_numberartists(dbmongo,
                                                                                          "RT_findDefinedArtistsnumber_artists",
                                                                                          cpu, memory, number_artists)

        # Histogram response_times count for artists number defined
        hist_rt_nartists(response_times_art_def, number_artists,
                         "Endpoint: findallartists" + "\nCPU: " + cpu + "\nMemory:" + memory, cpu)


def catch_rt_artist(dbmongo, collection, cpu, memory):
    dataset = []
    response_times = []
    number_artists = []
    items = ml.get_items_from_collection(dbmongo, collection, cpu, memory)
    for item in items:
        dataset.append(item)
    # It's important to shuffle the datasets
    random.shuffle(dataset)
    for item in dataset:
        number_artists.append(int(item['number_artists']))
        response_times.append(int(item['response_time']))
    return response_times, number_artists


def catch_response_times_by_numberartists(dbmongo, collection, cpu, memory, number_artists):
    items = ml.get_items_from_collection_by_numberartists(dbmongo, collection, cpu, memory, number_artists)
    response_times = []
    number_artists = []
    for item in items:
        number_artists.append(int(item['number_artists']))
        response_times.append(int(item['response_time']))
    return response_times, number_artists


if __name__ == "__main__":
    main()
