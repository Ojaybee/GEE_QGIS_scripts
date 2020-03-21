'''          
Script to create collections for Google Earth Engine plugin 
To be used in QGIS Python console
tutorial video available here: https://youtu.be/ODBCPmQBEqU

'''

# Authors: Oliver (http://www.burdgis.com)
# License: MIT


import ee 
import calendar
from datetime import datetime
from dateutil.relativedelta import *
from ee_plugin import Map 

dataset = 'COPERNICUS/S5P/NRTI/L3_NO2' # change to required dataset
column = 'NO2_column_number_density' # change to required column


# Styling for the layers
band_viz = {
  'min': 0,
  'max': 0.0002,
  'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
}

# accepts 2 str in numerical format YYYYmmdd e.g. 20190331
def getDates(startDate, endDate):
    
    startDate = datetime.strptime(startDate, '%Y%m%d')
    endDate = datetime.strptime(endDate, '%Y%m%d')
    
    counter = (endDate.year - startDate.year) * 12 + (endDate.month - startDate.month) + 1
    for d in range(counter):
        
        collName = "{:02d}".format(d) + "Collection"
        collStart = startDate + relativedelta(months=+d)
        finalDay = calendar.monthrange(collStart.year, collStart.month)[1]
        collEnd = collStart+relativedelta(day=finalDay)
        layerName = collStart.strftime("%b %Y")
        print(layerName)
                
        yield[collName, collStart.strftime("%Y-%m-%d"), collEnd.strftime("%Y-%m-%d"), layerName]

# change dates here        
for n in getDates('YYYYmmdd','YYYYmmdd'):
    n[0] = ee.ImageCollection(dataset)\
            .select(column)\
            .filterDate(n[1], n[2])
    Map.addLayer(n[0].mean(), band_viz, 'S5P N02 - ' + n[3] )
    

Map.setCenter(65.27, 24.11, 4)

