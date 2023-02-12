import csv

"""
This program reads the data of annual child deaths of several countries and regions of the world.
Data was obtained from data bank of the Banco Mundial published in the web:
(https://code.tutsplus.com/es/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907)
Author: Jairo Tovar C.
Written:     2022/10/20
Last update: 2023/02/10


- Data comes in a csv file (datos_muertes_infantiles.csv)
- Data could be read also using the Pandas library or NumPy, but I want to show step by step how it could be done
  through the basic tools provided by Python 
"""

# Read data and convert it to a dictionary:
separator = "," # this is the character that separates the fields
#datos_dict = {} # the dictionary where the data will be stored
datos_dict = dict()
#annualDeathQty = [] # stores the figures of annual deaths
#nameOfYear = [] # stores the name of each field representing the year of annual deaths data (1960 - 2020)
#for i in range(61):
#    nameOfYear[i] = str(i + 1961) # store the years from 1960 to 2020

data_file = 'Datos\datos_muertes_infantiles.csv'
with open(data_file, newline='') as File:
    reader = csv.reader(File)
    next(File)         # Ignore the first line because it contains titles (headers)
    #next(File)
    #next(File)
    #next(File)
    #next(File)
    j=1
    for row in reader: # process each line of the file
        # Reads each record in a list containing one element (just the linea read as a string). The line contains all
        # the fields
        #print(row)
       
        row[0] = row[0].rstrip("\n") # deletes the newline character at the end of the line
        #cols = row[0].split(separator)
        
        #if j == 1:
        #for k in range(67):
        #    print(k,"->",row[k]," ",end = "")
        
        #print("")
        #n = 1
        #cols = [row[i:i + n] for i in range(0, len(row), n)]
        #for i in range(0, len(row))
        #    col[i] = 
        countryName = row[0] # string
        countryCode = row[1] # string
        indicatorName = row[2] # string (unnecessary identifier)
        indicatorCode = row[3] # string (unnecessary identifier)
        # Fills the next 61 fields with the annual number of child deaths of the country (data are stored in cols[4] to cols[64]):
        #for i in range(4, 65):
        #    annualDeathQty_dict = {nameOfYear[i-4]:int(cols[i]) for i in range(4, 65)}
        
        #The data read are stored in the datos_dict dictionary using the countryCode as a key.
        #Each entry of the datos_dict dictionary contains its key (countryCode) and 62 values stored in a list, as follows:
        #- countryName (string)
        #- 61 int values corresponding to the figures for 61 years (1960 to 2020) of deaths information

        # Add one entry to the datos_dict dictionary:
        datos_dict[countryCode] = [countryName] # add the Country Name to the list of values
        for i in range(4, 65):
            #datos_dict[countryCode].append(int(cols[i])) # add each one of the annual values
            #print(type(row[i]))
            datos_dict[countryCode].append(row[i]) # add each one of the annual values to the list that stores the data of this country
            #print(cols[i])
        
        #if countryCode == "ARE":
        #    #print(datos_dict)
        #    print(datos_dict.get('ARE'))
        #print(countryCode)
        j += 1
    File.close()

"""
Now, we can analyze the data, processing the individual values of each key of the dictionary, for example,
we will find the mean, the standard deviation, the máximum and the minimum for all the data (number of deaths)
"""
# Go through the datos_dict:

#for item in datos_dict.items():
#    for i in range(4, 65):
#        print(item[i][1])
#        totalDeaths = totalDeaths + item[i][1]

# Calculate the total deaths in the period 1960 to 2020 and other global statistics:
totalDeaths = 0
numItems = 0
numRecords = 0
numCountriesWithData = 0
for codPais in datos_dict:
    #lista = datos_dict[codPais]
    #print(codPais)
    numRecords += 1
    thisCountryHasData = False
    for i in range(1, 62):
        if datos_dict[codPais][i].isdigit():
            totalDeaths += int(datos_dict[codPais][i])
            numItems += 1
            thisCountryHasData = True
    
    if thisCountryHasData:
        numCountriesWithData += 1
    
print("Total Children death during the period 1960 - 2020: ", f'{totalDeaths:,}')
print("Number of records with data: ", f'{numCountriesWithData:,}')
print("Number of items (years) included in the statistics: ", f'{numItems:,}')

# Calculate which country had the maximum number of deaths in the period 1960 to 2020,
# Calculate which country had the minimum number of deaths in the period 1960 to 2020:
numMax = 0
countryMax = ""
numMin = 1000000000
countryMin = ""
for codPais in datos_dict:
    #lista = datos_dict[codPais]
    #print(codPais)
    #thisCountryHasData = False
    totalDeathsInPeriod = 0
    num = 0
    for i in range(1, 62):
        if datos_dict[codPais][i].isdigit():
            totalDeathsInPeriod += int(datos_dict[codPais][i])
            num += 1
    
    if totalDeathsInPeriod > numMax:
        numMax = totalDeathsInPeriod
        countryMax = datos_dict[codPais][0]

    if totalDeathsInPeriod < numMin:
        if num == 61: # It counts for the minimum only if its statistic is complete for the period!
            numMin = totalDeathsInPeriod
            countryMin = datos_dict[codPais][0]

print("Country with the maximum number of deaths in the period 1960 - 2020: ", countryMax, "(", f'{numMax:,}', "deaths)")
print("Country with the minimum number of deaths in the period 1960 - 2020: ", countryMin, "(", f'{numMin:,}', "deaths)")
print("* For this mark only are included the countries with complete data for the period, because there are"
print("  countries with incomplete data including countries without data at all")
print("")
print("Countries and others included in the analysis:")
for codPais in datos_dict:
    #print(codPais)
    print(datos_dict[codPais][0])

print("Total records: ", f'{numRecords:,}')
