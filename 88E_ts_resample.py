# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:30:03 2019 @author: AKHIL Poojary
"""

#Dates  - Range
#-----------------------------
#https://towardsdatascience.com/playing-with-time-series-data-in-python-959e2485bff8

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

dtrange1D = pd.date_range('2019-1-1', '2019-7-11', freq='D')
dtrange1D
dtrange1D.min()


#The resulting DatetimeIndex has an attribute freq with a value of 'D', indicating daily frequency.#Available frequencies in pandas include 
#hourly ('H'), 
#calendar daily ('D'),
#business daily ('B'),
#weekly ('W'),
#monthly ('M'),
#quarterly ('Q'),
#annual ('A'), and many others.
#Frequencies can also be specified as multiples of any of the base frequencies, for example '5D' for every five days.

dtrange3D = pd.date_range('2019-1-1', '2019-7-11', freq='3D')
dtrange3D

dtrange1M = pd.date_range('2019-1-1', '2019-7-11', freq='1M')
dtrange1M

#date range at hourly frequency, specifying the start date and number of periods, instead of the start date and end date.

pd.date_range('2019-7-11', periods=8, freq='H')
pd.date_range('2019-7-11 09:00', periods=8, freq='H')

#https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/
#convert to different freq
#create data frame - weekly freq with some data
classStrength = np.random.randint(25,60, size=100)
classStrength
weekdates = pd.date_range('2019-5-1', periods=100, freq='B')
weekdates
attendance = pd.DataFrame({'classStr':classStrength, 'wdates':weekdates})
attendance.head(10).append(attendance.tail(10))

#
attendance.set_index('wdates', inplace=True)
attendance
#create another column with daily freq
attendance.asfreq('D')  #some missing values Sat/ Sun : REPLACES WITH NAN
attendance.head(10)
#temporarily creates dates for Sat/ Sun, fill with NA

#del dailyAttendance
attendance.asfreq('D', method='ffill')
attendance.head(9)
daily1 = attendance.asfreq('D', method='bfill')
daily1.head(10)
#replace permanently
daily1.rename(columns= {'classStr':'Daily_attendance'}, inplace=True)
daily1.head(10)
newAttendance2 = pd.concat([attendance, daily1], axis=1)
newAttendance2.head(10)

#a.to_frame().join(b)#with same index
#resample
newAttendance2.resample('W').sum()
newAttendance2.resample('W').mean()
newAttendance2.resample('M').sum()
newAttendance2.resample('bQ').mean()

newAttendance2.columns
newAttendance2.classStr
newAttendance2.Daily_attendance

#
# Start and end of the date range to extract
start, end = '2019-05', '2019-06'
# Plot daily and weekly resampled time series together
#run together upto plt.show
fig, ax = plt.subplots(figsize=(25,8))
ax.plot(newAttendance2.loc[start:end, 'Daily_attendance'], marker='.', linestyle=':', linewidth=1, label='Daily')
ax.plot(newAttendance2.loc[start:end, 'classStr'], marker='o', markersize=1, linestyle='--', label='Actual Attendance')
ax.set_ylabel('Class Strength')
plt.xticks(rotation=90)
ax.legend()
plt.show();

#------------------------------------

#
newAttendance2['Daily_attendance'].resample('M').sum()
newAttendance2.index.max() # command to find the last working day in the dataset
newAttendance2['Daily_attendance'].resample('M').sum(min_count=14)
# min_count = Minimum rows for the month : Minimum classes held in the month
# Wherever daily attendance is >12, its only counting those rows.
#min rows=5

#----------
fig, ax = plt.subplots(figsize=(25,8))
ax.plot(newAttendance2['Daily_attendance'], color='black', label='Daily Attendance')
newAttendance2[['classStr','Daily_attendance']].plot.area(ax=ax, linewidth=0)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.legend()
ax.set_ylabel('Student Strength')
plt.show();


#https:aquest.io/blog/tutorial-time-se//www.datries-analysis-with-pandas/
#resample() method, which splits the DatetimeIndex into time bins and groups the data by time bin