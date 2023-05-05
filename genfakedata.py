import numpy as np
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily
from meteostat import Hourly
# Import Meteostat library
from meteostat import Stations
import pandas
import random

def fetch():
    # Get nearby weather stations
    stations = Stations()
    stations = stations.nearby(45.6815, -111.0320)
    station = stations.fetch(3)
    start = datetime(2022,1,1)
    end = datetime(2022,12,31)
    data = Hourly('KEKS0', start, end)
    data = data.fetch()
    print(data)
    # Print DataFrame
    data.to_csv('fake_data3.csv')

#KBZN0
#KLVM0
#KEKS0

#with open('fakedata.csv', 'w') as file:
#    file.close()

def genfake():
    #offsets
        #direct offsets
        #date/time based offsets
        #add multiploer
        #general noise
    df = pandas.read_csv("sc1.csv")
    #df.loc[row_indexer,column_indexer]

    for label, content in df.items():
        print(content[1])



       
# AI will predict the weather in the following hours, maybe hour 1, 2, 3, 4, 5, 6
# need to check these values at a fake(measured) data index, match that index to historical data and get
# hours 1 - 6 from historical data

genfake()