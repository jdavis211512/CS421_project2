import pandas as pd
import matplotlib.pyplot as plot
from datetime import datetime


#C:\Users\jdavi\PycharmProjects\CS421_project2\project 2
def readCSV(filepath):
    choice = input("what company are you wanting to view?\n")
    choice.lower()
    if (choice == "amazon"):
        dateCols = ['Date']
        return pd.read_csv(filepath,parse_dates=dateCols)
    if(choice == "apple"):
        dateCols = ['Date']
        return pd.read_csv(filepath,parse_dates=dateCols)
    if (choice == "google",):
        dateCols = ['Date']
        return pd.read_csv(filepath,parse_dates=dateCols)
    else:
        print("please choose one of the 3 files for the assignment.")
        return readCSV(filepath)

def chooseFrame(dataframe):

    year = input("what is the year you want to see?\n")
    if (year=="2015"):
        return pd.date_range('2015-10-23','2015-12-31')
    if (year=="2016"):
        return pd.date_range('2016-1-1','2016-12-31')
    if (year=="2017"):
        return pd.date_range('2017-1-1','2017-12-31')
    if (year=="2018"):
        return pd.date_range('2018-1-1', '2018-12-31')
    if (year=="2019"):
        return pd.date_range('2019-1-1','2019-12-31')
    if (year=="2020"):
        return pd.date_range('2020-1-1', '2020-10-22')
    else:
        print("please select a year")
        chooseFrame(dataframe)

def plotthis(minimum,maximum,closing,date):
    plot.plot(date,minimum,color='blue')
    plot.plot(date,maximum, color='red')
    plot.plot(date,closing,color='black')
    plot.show()
    # plot.plot(date,)
def getmeans():


def main():
    filepath = input("what is the filepath of the file you want to use?\n")
    data = readCSV(filepath)
    yearRange = chooseFrame(data)
    fixedFrame = data[data['Date'].isin(yearRange)]
    minimumSeries = fixedFrame['Low']
    maximumSeries = fixedFrame['High']
    dailySeries = fixedFrame['Close']
    dateSeries = fixedFrame['Date']
    meanSeries = getmeans()
    plotthis(minimumSeries,maximumSeries,dailySeries,dateSeries)







if __name__ == '__main__':
    main()