import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

covid_data = pd.read_csv("full_data.csv") #The code for importing the .csv file works
os.chdir("/users/Nothung/IBI1_2021-22/IBI1_2021-23/Practical7")

print(covid_data.iloc[9:20,[0,2]]) #showing the first and third columns from rows 10-20 (inclusive)

for i in range (0,7996): #“total cases” for all rows corresponding to Afghanistan.
    if covid_data.iloc[i,1]=="Afghanistan":
       print (covid_data.loc[i,"total_cases"])

china_covid_data = pd.read_csv("china_data.csv")

print(china_covid_data.mean()) #the mean number of new cases and new deaths in China.

#a boxplot of new cases and new deaths in China worldwide.
n=92
plt.boxplot(china_covid_data.loc[:,"new_cases"],
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.title("boxplot of new cases in China")
plt.show()

n=92
plt.boxplot(china_covid_data.loc[:,"new_deaths"],
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.title("boxplot of new deaths in China")
plt.show()

china_dates = pd.read_csv("china_dates.csv")

#plot both new cases and new deaths in China over time.
dates=china_dates.loc[:,"date"]
new_cases=china_covid_data.loc[:,"new_cases"]
new_deaths=china_covid_data.loc[:,"new_deaths"]

plt.plot(dates, new_cases, 'b+')
plt.plot(dates, new_deaths, 'r+')
plt.xticks(dates.iloc[0:len(dates):4],rotation=-90)
plt.title("new cases and new deaths in China over time")
plt.show()

#Question.
spain_data = pd.read_csv("Spain_data.csv")
spain_dates=spain_data.loc[:,"date"]
spain_new_cases=spain_data.loc[:,"new_cases"]
spain_total_cases=spain_data.loc[:,"total_cases"]

plt.plot(spain_dates,spain_new_cases,'b+')
plt.plot(spain_dates,spain_total_cases,'r+')
plt.xticks(dates.iloc[0:len(dates):4],rotation=-90)
plt.title("new cases and total cases in Spain over time")
plt.show()
