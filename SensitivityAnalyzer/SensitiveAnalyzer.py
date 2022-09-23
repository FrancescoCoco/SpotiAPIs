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
    cpu = "default"
    memory = "default"

    # Connection to the mongodb
    dbmongo = ml.mongo_auth()

    # Catch dataset
    response_times, number_artist = catch_rt_artist(dbmongo, 'RT_FindAllArtists', cpu, memory)

    # plot original model
    scatterplot_model(number_artist, response_times, "Endpoint: findallartists"
                      + "\nCPU: " + cpu + "\nMemory:" + memory,
                      "number artists", "response time(ms)")

    # linear regression
    linear_regression(number_artist, response_times, "Linear Regression\nEndpoint: findallartists"
                      + "\nCPU: " + cpu + "\nMemory:" + memory, "number artists", "response time(ms)")

    # POLYNOMIAL REGRESSIONS
    # Choose number of polynomial regression that you want to plot
    print("\nBefore to plot polynomial regressions, choose the number of polynomial regressions that you want to plot: (Minimum 1)" )
    number_plot_pr = int(input())

    if number_plot_pr == 0:
        number_plot_pr = 1

    x = 1
    while x <= number_plot_pr:
        print("Choose degree of polynomial regression: Minimum 2, Maximum 8 ")
        degree = int(input())
        if degree < 2 or degree > 8:
            degree = 2 # parameter to express the degree of polynomial regression
        polynomial_regression(number_artist, response_times, "Polynomial Regression\nEndpoint: findallartists"
                              + "\nCPU: " + cpu + "\nMemory:" + memory, "number artists", "response time(ms)", degree)

        x = x + 1

    # Question if you want to plot  response times associated with a number of artists defined
    print("\nWrite y or Y if you want to plot histogram of response times of a particular number of artists")
    defined_artists = str(input())

    if defined_artists == 'y' or defined_artists == "Y":
        print("Write number artists ")
        number_artists = int(input())
        # Fetch response times associated with a number of artists required, defined
        response_times_art_def, number_artist_def = catch_response_times_by_numberartists(dbmongo,
                                                                                          "RT_findDefinedArtistsnumber_artists",
                                                                                          cpu, memory, number_artists)

        # Histogram response_times count for artists number defined
        hist_rt_nartists(response_times_art_def, number_artists,
                         "Endpoint: findallartists" + "\nCPU: " + cpu + "\nMemory:" + memory, cpu)


# Get the response time of artists
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
