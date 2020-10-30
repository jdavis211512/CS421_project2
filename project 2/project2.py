import pandas as pd
import matplotlib.pyplot as plot
import numpy
from datetime import datetime


# C:\Users\jdavi\PycharmProjects\CS421_project2\project 2
# C:\Users\Hunter\OneDrive - Ball State University\Classes\Fall 2020\CS 421\CS421_project2\project 2\GOOGL.csv
def readCSV(filepath):
    choice = input("what company are you wanting to view?\n")
    choice.lower()
    dateCols = ['Date']
    if choice == "amazon":
        return pd.read_csv(filepath, parse_dates=dateCols)
    if choice == "apple":
        return pd.read_csv(filepath, parse_dates=dateCols)
    if choice == "google":
        return pd.read_csv(filepath, parse_dates=dateCols)
    else:
        print("please choose one of the 3 files for the assignment.")
        return readCSV(filepath)


def chooseFrame(dataframe):
    year = input("what is the year you want to see?\n")
    if year == "2015":
        return pd.date_range('2015-10-23', '2015-12-31')
    if year == "2016":
        return pd.date_range('2016-1-1', '2016-12-31')
    if year == "2017":
        return pd.date_range('2017-1-1', '2017-12-31')
    if year == "2018":
        return pd.date_range('2018-1-1', '2018-12-31')
    if year == "2019":
        return pd.date_range('2019-1-1', '2019-12-31')
    if year == "2020":
        return pd.date_range('2020-1-1', '2020-10-22')
    else:
        print("please select a year")
        chooseFrame(dataframe)


def visualizeYear(minimum, maximum, closing, date):
    plot.plot(date, minimum, color='blue')
    plot.plot(date, maximum, color='red')
    plot.plot(date, closing, color='black')
    plot.show()
    # plot.plot(date,)


# Stuff for Feature 2 - Min, Max, Average Box plot
def plotBox(close):
    minimum = close.min()
    maximum = close.max()
    average = close.mean()
    print("Minimum", minimum)
    print("Maximum", maximum)
    print("Average", average)
    plot.boxplot(close)
    plot.xlabel("Close")
    plot.ylabel("Close Price")
    plot.show()

# Stuff for Feature 3 - Regression Line
def my_mean(m):
    total = 0.0
    for x in m:
        total = total + float(x)
    return float(total) / len(m)


def my_w0(X, Y):
    mean_y = my_mean(Y)
    mean_x = my_mean(X)
    return mean_y - my_w1(X, Y) * mean_x


def my_w1(X, Y):
    x_mean = my_mean(X)
    y_mean = my_mean(Y)
    num = 0.0
    den = 0.0
    for i in range(X.idxmin(), X.idxmax()):
        num = num + (X[i] - x_mean) * (Y[i] - y_mean)
        den = den + (X[i] - x_mean) * (X[i] - x_mean)
    return num / den


def plotRegression(X, Y):
    plot.plot(X, Y, 'bo')
    plot.xlabel('Open Price')
    plot.ylabel('Close Price')
    w1 = my_w1(X, Y)
    w0 = my_w0(X, Y)
    y_estimated = []
    for x in X:
        y = w1 * x + w0
        y_estimated.append(y)
    x_samples = numpy.linspace(int(X.min()), int(X.max()), int(X.max()))
    y_samples = []
    for x in x_samples:
        y_samples.append(w0 + w1 * x)
    plot.plot(x_samples, y_samples, color='red')
    plot.show()


def main():
    filepath = input("what is the filepath of the file you want to use?\n")
    data = readCSV(filepath)
    yearRange = chooseFrame(data)
    fixedFrame = data[data['Date'].isin(yearRange)]
    # minimumSeries = fixedFrame['Low']
    # maximumSeries = fixedFrame['High']
    # dailySeries = fixedFrame['Close']
    # dateSeries = fixedFrame['Date']
    # meanSeries = getmeans()
    # visualizeYear(minimumSeries, maximumSeries, dailySeries, dateSeries)
    print("Feature 2")
    plotBox(fixedFrame['Close'])
    print("Feature 3")
    plotRegression(fixedFrame['Open'], fixedFrame['Close'])


if __name__ == '__main__':
    main()
