import pandas as pd
import csv
import random
import matplotlib.pyplot as plt
from skimage import io
#import urllib


#Import COVID deaths data from https://data.cdc.gov/NCHS/Provisional-COVID-19-Deaths-by-Place-of-Death-and-/uggs-hy5q 
#Direct link to csv file: https://data.cdc.gov/api/views/uggs-hy5q/rows.csv 
df = pd.read_csv("https://raw.githubusercontent.com/Julia-almeida/Covid/main/cdc_covid_deaths_9_17_22.csv")
#Shrinking df by excluding unnecessary data:
startDate = df[df["Start Date"] == "01/01/2020"] #all the rows from df that have 01/01/2020 as starting date
endDate = startDate[startDate["End Date"] == "09/17/2022"]
totalDeaths = endDate[endDate["Place of Death"] == "Total - All Places of Death"]
#print(totalDeaths)

newFile = open("rowsNeeded.csv", 'w') #creating and opening the csv file for future data entry
writeToFile = csv.writer(newFile) #using writer() method for future data entry to newly created file

states = []
deaths = []
#since totalDeaths is a shrunk data frame (which is more complicated data structure than regular list,
#we have to use more complex for loop with it)
for i,row in totalDeaths.iterrows():
  writeToFile.writerow(row) #writing rows to rowsNeeded.csv, which will be a 2D array consisting of all these rows as separate lists
  states.append(row["State"])
  deaths.append(int(row["COVID-19 Deaths"]))
  
newFile.close()

print("COVID Deaths by State:")
states.pop(0) #removes the first element from the list
deaths.pop(0)
for i in range(len(states)):
  print(states[i]+':', deaths[i])
print()

abbrStates = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NYC','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','PR']

x = []
for i in range(1, len(states)+1):
  x.append(i)
#print(x)

colors = []
for i in range(len(states)):
  r = random.random()
  g = random.random()
  b = random.random()
  colors.append((r,g,b))
#print(colors)

#Plot COVID Deaths for each state:
plt.figure(figsize=(11, 5), dpi=100)
plt.bar(x, deaths, width=0.8, color=colors)
plt.xticks(x, abbrStates, rotation='vertical')
plt.xlabel('States')
plt.ylabel('Deaths')
plt.title('COVID-Related Deaths by State')
plt.show()

#The population.csv uses data from https://data.census.gov/cedsci/table?tid=PEPPOP2021.NST_EST2021_POP&hidePreview=false 
population_df = pd.read_csv("https://raw.githubusercontent.com/Julia-almeida/Covid/main/population.csv")
population = []
for i,row in population_df.iterrows():
  population.append(int(row[1]))

deathPercent = []
#Propotions:
#population = 100
#deaths     =  ?
#? = deaths * 100 / population
for i in range(len(deaths)):
  deathPercent.append(deaths[i]*100/population[i])
#print(deathPercent)

print()

#Plot COVID Death Rates for each state:
plt.figure(figsize=(11, 5), dpi=100)
plt.bar(x, deathPercent, width=0.8, color=colors)
plt.xticks(x, abbrStates, rotation='vertical')
plt.xlabel('States')
plt.ylabel('Death Rates')
plt.title('COVID Death Rates by State')
plt.show()


#Embedding a line chart with COVID Deaths:
print()
print()
img = io.imread('https://raw.githubusercontent.com/btete/Covid/main/us-covid-deaths.png')
plt.figure(figsize=(12, 8), dpi=100)
plt.imshow(img)
plt.axis('off')
plt.title("Daily Trends in Number of COVID-19 Deaths in The United States Reported to CDC")
plt.show()


# New Section
