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

'''
jan19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-01-01', '2019-01-31')

feb19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-02-01', '2019-02-28')

mar19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-03-01', '2019-03-31')

apr19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-04-01', '2019-04-30')

may19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-05-01', '2019-05-31')

jun19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-06-01', '2019-06-30')

jul19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-07-01', '2019-07-31')

aug19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-08-01', '2019-08-31')

sep19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-09-01', '2019-09-30')

oct19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-10-01', '2019-10-31')

nov19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-11-01', '2019-11-30')
  
dec19Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2019-12-01', '2019-12-31')
  
jan20Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2020-01-01', '2020-01-31')
  
feb20Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2020-02-01', '2020-02-29')
  
mar20Collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
  .select('NO2_column_number_density') \
  .filterDate('2020-03-01', '2020-03-15')
'''




'''
Map.addLayer(jan19Collection.mean(), band_viz, 'S5P N02 - Jan 2019')
Map.addLayer(feb19Collection.mean(), band_viz, 'S5P N02 - Feb 2019')
Map.addLayer(mar19Collection.mean(), band_viz, 'S5P N02 - Mar 2019')
Map.addLayer(apr19Collection.mean(), band_viz, 'S5P N02 - Apr 2019')
Map.addLayer(may19Collection.mean(), band_viz, 'S5P N02 - May 2019')
Map.addLayer(jun19Collection.mean(), band_viz, 'S5P N02 - Jun 2019')
Map.addLayer(jul19Collection.mean(), band_viz, 'S5P N02 - Jul 2019')
Map.addLayer(aug19Collection.mean(), band_viz, 'S5P N02 - Aug 2019')
Map.addLayer(sep19Collection.mean(), band_viz, 'S5P N02 - Sep 2019')
Map.addLayer(oct19Collection.mean(), band_viz, 'S5P N02 - Oct 2019')
Map.addLayer(nov19Collection.mean(), band_viz, 'S5P N02 - Nov 2019')
Map.addLayer(dec19Collection.mean(), band_viz, 'S5P N02 - Dec 2019')

Map.addLayer(jan20Collection.mean(), band_viz, 'S5P N02 - Jan 2020')
Map.addLayer(feb20Collection.mean(), band_viz, 'S5P N02 - Feb 2020')
Map.addLayer(mar20Collection.mean(), band_viz, 'S5P N02 - Mar 2020')
'''

