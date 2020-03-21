import ee 
import calendar
from datetime import datetime
from dateutil.relativedelta import *
from ee_plugin import Map 

band_viz = {
  'min': 0,
  'max': 0.0002,
  'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
}

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
        
for n in getDates('20190101','20200320'):
    n[0] = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2')\
            .select('NO2_column_number_density')\
            .filterDate(n[1], n[2])
    Map.addLayer(n[0].mean(), band_viz, 'S5P N02 - ' + n[3] )
    

Map.setCenter(65.27, 24.11, 4)

