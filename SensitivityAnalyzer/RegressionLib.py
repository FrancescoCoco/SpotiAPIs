"""
██████╗░███████╗░██████╗░██████╗░███████╗░██████╗░██████╗██╗░█████╗░███╗░░██╗██╗░░░░░██╗██████╗░
██╔══██╗██╔════╝██╔════╝░██╔══██╗██╔════╝██╔════╝██╔════╝██║██╔══██╗████╗░██║██║░░░░░██║██╔══██╗
██████╔╝█████╗░░██║░░██╗░██████╔╝█████╗░░╚█████╗░╚█████╗░██║██║░░██║██╔██╗██║██║░░░░░██║██████╦╝
██╔══██╗██╔══╝░░██║░░╚██╗██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗██║██║░░██║██║╚████║██║░░░░░██║██╔══██╗
██║░░██║███████╗╚██████╔╝██║░░██║███████╗██████╔╝██████╔╝██║╚█████╔╝██║░╚███║███████╗██║██████╦╝
╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝╚═════╝░
"""

import matplotlib.pyplot as plt
import numpy
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures


# Scatter plot model
def scatterplot_model(x, y, plot_titles, x_name, y_name):
    # plotting the model
    plt.figure(figsize=(5, 7))
    plt.scatter(x, y, color='black')

    # naming the x axis
    plt.xlabel(x_name)

    # naming the y axis
    plt.ylabel(y_name)

    # giving a title to my graph
    plt.title(plot_titles)

    # function to show the plot
    plt.show()


# Linear Regression
def linear_regression(X, y, plot_title, x_name, y_name):
    X = numpy.array(X).reshape(-1, 1)
    y = numpy.array(y)
    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train model using training sets
    new_model = regr.fit(X_train, y_train)

    # Make predicion
    y_pred = regr.predict(X_test)

    # PRINT RESULTS
    print("\nLinear Regression:")
    # Coefficients
    print("Coefficients:", regr.coef_)

    # Mean Squared Error
    print(f"Mean Squared error: {mean_squared_error(y_test, y_pred)}")

    # Coefficient of determination: 1 is perfect
    print(f"coefficient of determination: {r2_score(y_test, y_pred)}")

    # Intercept
    print(f"intercept: {new_model.intercept_}")

    # PLOT
    plt.figure(figsize=(5, 7))

    plt.scatter(X_train, y_train, color="red", label="train")
    plt.scatter(X_test, y_test, color="blue", label="test")
    plt.plot(X_test, y_pred, color="black", label="prediction")

    plt.text(400, 170, "MSE: " + str(round(mean_squared_error(y_test, y_pred), 3)), fontsize=10)
    plt.text(400, 165, "r2_score: " + str(round((r2_score(y_test, y_pred)), 3)), fontsize=10)
    plt.text(400, 160, "Intercept: " + str(round(new_model.intercept_, 3)), fontsize=10)

    # Plot Output

    # Plot Annotations

    # plt.annotate("Coefficients: ", regr.coef_)

    # plt.annotate(f"intercept: {new_model.intercept_}")

    # Position of the legend
    plt.legend(loc="lower right")

    # naming the x axis
    plt.xlabel(x_name)
    # naming the y axis
    plt.ylabel(y_name)

    # giving a title to my graph
    plt.title(plot_title)

    plt.show()


#  Polynomial regression
def polynomial_regression(X, y, plot_title, x_name, y_name):
    X = numpy.array(X).reshape(-1, 1)
    y = numpy.array(y)

    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    poly_regr = PolynomialFeatures(degree=5)  # our polynomial model is of order
    X_poly = poly_regr.fit_transform(X)  # transforms the features to the polynomial form

    lin_reg_2 = linear_model.LinearRegression()  # creates a linear regression object
    model = lin_reg_2.fit(X_poly, y)  # fits the linear regression object to the polynomial features

    # target predict
    y_pred = lin_reg_2.predict(poly_regr.fit_transform(X))

    # Coefficient of determination
    r_sq = model.score(X_poly, y)

    # Intercept and coefficients
    intercept, coefficients = model.intercept_, model.coef_

    # Print value
    print("\nPolynomial regression:")
    print(f"Mean Squared error: {mean_squared_error(y, y_pred)}")
    print(f"Coefficient of determination: {r_sq}")
    print(f"Intercept: {intercept}")

    plt.figure(figsize=(5, 7))

    # Scatter output
    plt.scatter(X_train, y_train, color='red', label="train")  # plotting the training set
    plt.scatter(X_test, y_test, color='blue', label="test")  # plotting the test set
    plt.scatter(X, y_pred, color='black', label="prediction")

    plt.text(400, 170, "MSE: " + str(round(mean_squared_error(y, y_pred), 3)), fontsize=10)
    plt.text(400, 165, "r2_score: " + str(round(r_sq, 3)), fontsize=10)
    plt.text(400, 160, "Intercept: " + str(round(intercept, 3)), fontsize=10)

    # naming the x axis
    plt.xlabel(x_name)
    # naming the y axis
    plt.ylabel(y_name)

    # Position of the legend
    plt.legend(loc="lower right")

    # giving a title to my graph
    plt.title(plot_title)

    plt.show()


def hist_rt_nartists(response_times_art_def):
    df = pd.DataFrame({'response_times': response_times_art_def})
    dfp = df.pivot_table(index='response_times', aggfunc='size')
    dfp.plot(kind='bar', figsize=(7, 5), rot=0,)
    # naming the x axis
    plt.xlabel("response times(ms)")
    # naming the y axis
    plt.ylabel("count")
    plt.title("Response Times counts")
    plt.show()
