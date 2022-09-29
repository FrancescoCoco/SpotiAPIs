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
from RegressionLib import scatterplot_model, linear_regression, polynomial_regression, hist_rt_nartists, hist_rt_nalbums


def main():
    cpu = "0.005"
    memory = "default"

    # Connection to the mongodb
    dbmongo = ml.mongo_auth()

    """ARTIST"""
    print(
        "\nWrite y or Y if you want to plot the linear regression and non linear regression of response times endpoint findallartists")
    plot_artist = input()
    if plot_artist == 'y' or plot_artist == 'Y':
        # Catch dataset
        response_times, number_artist = catch_rt_artist(dbmongo, 'RT_FindAllArtists', cpu, memory)

        # plot original model
        scatterplot_model(number_artist, response_times, "Endpoint: findallartists"
                          + "\nCPU: " + cpu + "\nMemory:" + memory,
                          "number artists", "response time(ms)")

        # linear regression
        linear_regression(number_artist, response_times, "Linear Regression\nEndpoint: findallartists"
                          + "\nCPU: " + cpu + "\nMemory:" + memory, "number artists", "response time(ms)", 400, 150)

        # NON LINEAR  REGRESSIONS
        # Choose number of non linear  regression that you want to plot
        print(
            "\nBefore to plot non linear regressions, choose the number of non linear regressions that you want to plot: (Minimum 1)")
        number_plot_pr = int(input())

        if number_plot_pr == 0:
            number_plot_pr = 1

        x = 1
        while x <= number_plot_pr:
            print("Choose degree of non linear regression: Minimum 2, Maximum 8 ")
            degree = int(input())
            if degree < 2 or degree > 8:
                degree = 2  # parameter to express the degree of non linear regression
            polynomial_regression(number_artist, response_times, "Non linear Regression\nEndpoint: findallartists"
                                  + "\nCPU: " + cpu + "\nMemory:" + memory, "number artists", "response time(ms)",
                                  degree, 400, 150)

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
                                                                                              cpu, memory,
                                                                                              number_artists)

            # Histogram response_times count for artists number defined
            bin_space = 100
            bin_width = 50
            hist_rt_nartists(response_times_art_def, number_artists,
                             "Endpoint: findallartists" + "\nCPU: " + cpu + "\nMemory:" + memory, cpu, bin_space,
                             bin_width)

    """ALBUMS"""
    
    print(
        "\nWrite y or Y if you want to plot the linear regression and non linear regression of response times endpoint findallalbums")
    plot_albums = input()
    if plot_albums == 'y' or plot_albums == 'Y':

        # Catch dataset
        response_times_alb, number_albums = catch_rt_albums(dbmongo, 'RT_FindAllAlbums', cpu, memory)

        # plot original model
        scatterplot_model(number_albums, response_times_alb, "Endpoint: findallalbums"
                          + "\nCPU: " + cpu + "\nMemory:" + memory,
                          "number albums", "response time(ms)")
        # linear regression
        linear_regression(number_albums, response_times_alb, "Linear Regression\nEndpoint: findallalbums"
                          + "\nCPU: " + cpu + "\nMemory:" + memory, "number albums", "response time(ms)", 100, 30)

        # non linear  REGRESSIONS
        # Choose number of non linear regression that you want to plot
        print(
            "\nBefore to plot non linear  regressions, choose the number of non linear regressions that you want to plot: (Minimum 1)")
        number_plot_pr = int(input())

        if number_plot_pr == 0:
            number_plot_pr = 1

        x = 1
        while x <= number_plot_pr:
            print("Choose degree of non linear regression: Minimum 2, Maximum 8 ")
            degree = int(input())
            if degree < 2 or degree > 8:
                degree = 2  # parameter to express the degree of non linear regression
            polynomial_regression(number_albums, response_times_alb, "non linear Regression\nEndpoint: findallartists"
                                  + "\nCPU: " + cpu + "\nMemory:" + memory, "number albums", "response time(ms)",
                                  degree, 100, 30)

            x = x + 1

        # Question if you want to plot  response times associated with a number of artists defined
        print("\nWrite y or Y if you want to plot histogram of response times of a particular number of albums")
        defined_albums = str(input())

        if defined_albums == 'y' or defined_albums == "Y":
            print("Write number albums ")
            number_album = int(input())
            # Fetch response times associated with a number of artists required, defined
            response_times_alb_def, number_albums_def = catch_response_times_by_numberalbums(dbmongo,
                                                                                             "RT_findDefinedAlbumsnumber_albums",
                                                                                             cpu, memory,
                                                                                             number_album)

            # Histogram response_times count for artists number defined
            bin_space = 10
            bin_width = 1
            hist_rt_nalbums(response_times_alb_def, number_album,
                            "Endpoint: findallalbums" + "\nCPU: " + cpu + "\nMemory:" + memory, cpu, bin_space,
                            bin_width)

    print(
        "\nWrite y or Y if you want to plot the linear regression and non linear regression of response times endpoint findallalbums optimized")
    plot_albums = input()
    if plot_albums == 'y' or plot_albums == 'Y':
        # Catch dataset
        response_times_alb, number_albums = catch_rt_albums(dbmongo, 'Response_times_optimized_albums', cpu, memory)

        # plot original model
        scatterplot_model(number_albums, response_times_alb, "Endpoint: findallalbums"
                          + "\nCPU: " + cpu + "\nMemory:" + memory,
                          "number albums", "response time(ms)")
        # linear regression
        linear_regression(number_albums, response_times_alb, "Linear Regression\nEndpoint: findallalbums"
                          + "\nCPU: " + cpu + "\nMemory:" + memory, "number albums", "response time(ms)", 100, 30)

        # non linear  REGRESSIONS
        # Choose number of non linear regression that you want to plot
        print(
            "\nBefore to plot non linear  regressions, choose the number of non linear regressions that you want to plot: (Minimum 1)")
        number_plot_pr = int(input())

        if number_plot_pr == 0:
            number_plot_pr = 1

        x = 1
        while x <= number_plot_pr:
            print("Choose degree of non linear regression: Minimum 2, Maximum 8 ")
            degree = int(input())
            if degree < 2 or degree > 8:
                degree = 2  # parameter to express the degree of non linear regression
            polynomial_regression(number_albums, response_times_alb, "non linear Regression\nEndpoint: findallartists"
                                  + "\nCPU: " + cpu + "\nMemory:" + memory, "number albums", "response time(ms)",
                                  degree, 100, 30)

            x = x + 1




# Get the response time of artists
def catch_rt_artist(dbmongo, collection, cpu, memory):
    response_times = []
    number_artists = []
    items = ml.get_items_from_collection(dbmongo, collection, cpu, memory)
    for item in items:
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


# Get the response time of albums
def catch_rt_albums(dbmongo, collection, cpu, memory):
    response_times = []
    number_albums = []
    items = ml.get_items_from_collection(dbmongo, collection, cpu, memory)
    for item in items:
        number_albums.append(int(item['number_albums']))
        response_times.append(int(item['response_time']))
    return response_times, number_albums


def catch_response_times_by_numberalbums(dbmongo, collection, cpu, memory, number_albums):
    items = ml.get_items_from_collection_by_numberalbums(dbmongo, collection, cpu, memory, number_albums)
    response_times = []
    number_albums = []
    for item in items:
        number_albums.append(int(item['number_albums']))
        response_times.append(int(item['response_time']))
    return response_times, number_albums


if __name__ == "__main__":
    main()
