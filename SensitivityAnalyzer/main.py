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
    # Connection to the mongodb
    dbmongo = ml.mongo_auth()
    cpu = "1"
    response_times, number_artist = catch_rt_artist(dbmongo, 'RT_FindAllArtists', cpu)

    # plot original model
    scatterplot_model(number_artist, response_times, "Endpoint: findallartists"
                      + "\nCPU: " + cpu,
                      "number artists", "response time(ms)")

    # linear regression
    linear_regression(number_artist, response_times, "Linear Regression\nEndpoint: findallartists"
                      + "\nCPU: " + cpu, "number artists", "response time(ms)")

    # polynomial regression
    polynomial_regression(number_artist, response_times, "Polynomial Regression\nEndpoint: findallartists"
                          + "\nCPU: " + cpu, "number artists", "response time(ms)")

    # Model the response times with a certain number of endpoints
    number_artists = 3000
    defined_artist = True

    # Variable to set after firts plot, default NONE !!
    if defined_artist:
        response_times_art_def, number_artist_def = catch_response_times_by_numberartists(dbmongo,
                                                                                          "RT_findDefinedArtistsnumber_artists",
                                                                                          cpu, number_artists)

        # Histogram response_times count for artists number defined
        hist_rt_nartists(response_times_art_def, number_artists, "Endpoint: findallartists", cpu)


def catch_rt_artist(dbmongo, collection, cpu):
    dataset = []
    response_times = []
    number_artists = []
    items = ml.get_items_from_collection(dbmongo, collection, cpu)
    for item in items:
        dataset.append(item)
    # It's important to shuffle the datasets
    random.shuffle(dataset)
    for item in dataset:
        number_artists.append(int(item['number_artists']))
        response_times.append(int(item['response_time']))
    return response_times, number_artists


def catch_response_times_by_numberartists(dbmongo, collection, cpu, number_artists):
    items = ml.get_items_from_collection_by_numberartists(dbmongo, collection, cpu, number_artists)
    response_times = []
    number_artists = []
    for item in items:
        number_artists.append(int(item['number_artists']))
        response_times.append(int(item['response_time']))
    return response_times, number_artists


if __name__ == "__main__":
    main()
