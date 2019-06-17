import csv
import sys
import statistics
import pandas as pd
import os

from datetime import datetime
import time
start_time = time.time()


class DataframePass:
    """
    Pass the pd DataFrame whenever creating instances of the class
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def readDataFrame(self):
        print(self.dataframe)
        return self.dataframe

def readCsvFile():
    """
    Read both the CSV file and 
    return both in Python Dataframe as tuple
    data1 "read pickup_times.csv and return dataframe"
    data2 "read locations.csv and return dataframe"
    """
    with open('csv/pickup_times.csv') as csvDataFile1: #open the CSV file
        data1 = pd.read_csv(csvDataFile1) #Data frame
        
    with open('csv/locations.csv') as csvDataFile2: #open the CSV file
        data2 = pd.read_csv(csvDataFile2) #Data frame
        
    return (data1, data2)
def takeDataframeReturnListofDataframes(data2):
    """
    Functions that takes a dataframe as input
    and returns list of dataframes that contains element of list as
    "dataframe containing row and column with same location_id "where
    column location_id equals to (1-85)

    """
    listi = [] #list to hold dataframes; element = dataframe with same location_id
    for i in range(1,(len(readCsvFile()[1]) + 1)): #len(readCsvFile()[1] = 85)
        location2 = data2[data2.location_id.isin([i])] #stores dataframe with location_id column equal 2 and respective pickuptimecolumn
       # print(location2)  
        listi.append(location2) 
    #print(listi)
    return listi
    
def askUserYearMonthDay():
    """
    Functions that ask user to enter year month and day 
    return date string
    """
    list = []
    year = str(input('Enter a year: '))
    list.append(year)
    month = str(input('Enter a month: '))
    list.append(month)
    day = str(input('Enter a day: '))
    list.append(day)
    starthour = str(input('Enter hour in HH format From when: '))
    list.append(starthour)
    stophour = str(input('Enter hour in HH format To : '))
    list.append(stophour)
    date = (list[0]+ "-"+list[1]+"-"+list[2]+ " "+ list[3]+":00"+ list[4]+":00")
    #print(date)2019-01-09 18:0019:00
    return date

def convertIsoTimestampDataToDateTimeFormat(dataframe):
    """
    Functions that converts the iso_8601_timestamp column's data
    to date time format and returns the dataframe.
    """
    dataframe = dataframe.copy()
    dataframe.loc[:, 'iso_8601_timestamp'] = pd.to_datetime(dataframe['iso_8601_timestamp'])
    return dataframe


def setIndexAsIso_8601_TimestampAndReturnListContainingItemAsTupleOfLocationAndMedian(dataframelist):
    """
    Functions that takes list as a parameter and take each element of list
    and convert the iso_8601_timestamp to date time and returns list with dataframe
    having iso_8601_timestamp as index
    """
    
    listi = []
    dm = askUserYearMonthDay()
    for i in range(len(dataframelist)):
        df3 = convertIsoTimestampDataToDateTimeFormat(dataframelist[i])
        df4 = df3.set_index('iso_8601_timestamp')
        df5 = df4[dm[0:10]]
        df6 = df5.between_time(dm[11:16], dm[16:21])
        df2Median = (df6.loc[:,"pickup_time"]).median()
        #d8 = DataframePass(readCsvFile()[1]).dataframe
        #d9 = (format(d8.iloc[i,1], '.6f'), format(d8.iloc[i,2], '.6f'))
        df7 =  (i+1, str(df2Median)) #, str(d9[0]), str(d9[1]))
        listi.append(df7)
        print(df6)
    return listi

def returnCSVfile(listi):
    """
    Function takes a list that contains tuple as a element
    Tuple first item is value for Location_id
    Second Item is value for medianpickuptime
    Open a CSV file and write 
    Column are named Location_id and medianpickuptime
    Returns None(which needs to be resolved)
    """
    with open('csv/mediantimes.csv', 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['location_id', 'medianpickuptime']) #,'longitude','latitude'])
        for row in listi:
            csv_out.writerow(row)
    return True  

dataframe = DataframePass(readCsvFile()[0]).dataframe    
dflist = takeDataframeReturnListofDataframes(dataframe)



dfmedian = setIndexAsIso_8601_TimestampAndReturnListContainingItemAsTupleOfLocationAndMedian(dflist)
returnCSVfile(dfmedian)
#print(dfmedian[0])
#d8 = DataframePass(readCsvFile()[1]).dataframe
#print(type(float(d8.iloc[0,1])))
#print("My program took", time.time() - start_time, "to run")


#print