import pandas as pd
import matplotlib.pyplot as plot
def readCSV(filepath):
    choice = input("what company are you wanting to view?\n")
    choice.lower()
    if (choice == "amazon"):
        return pd.read_csv(filepath)
    if(choice == "apple"):
        return pd.read_csv(filepath)
    if (choice == "google"):
        return pd.read_csv(filepath)
    else:
        print("please choose one of the 3 files for the assignment.")
        return readCSV()

def chooseFrame(dataframe):

    year = input("what is the year you want to see?\n")
    if (year=="2015"):
        return dataframe.iloc[0:47]
    if (year=="2016"):
        return dataframe.iloc[48:299]
    if (year=="2017"):
        return dataframe.iloc[300:550]
    if (year=="2018"):
        return dataframe.iloc[551:801]
    if (year=="2019"):
        return dataframe.iloc[802:1053]
    if (year=="2020"):
        return dataframe.iloc[1054:1258]
    else:
        print("please select a year")
        chooseFrame(dataframe)




def main():
    filepath = input("what is the filepath of the file you want to use?\n")
    data = readCSV(filepath)
    yearFrame = chooseFrame(data)






if __name__ == '__main__':
    main()