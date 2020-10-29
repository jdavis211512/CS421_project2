import pandas as pd
import matplotlib.pyplot as plot
def readCSV(filepath):
    dataframe = pd.read_csv(filepath)
    print(dataframe)

def rollingMean(dataframe):


def main():
    filepath = input("what is the filepath of the file you want to use?")
    data = readCSV(filepath)





if __name__ == '__main__':
    main()