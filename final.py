from tkinter.filedialog import *
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

data = askopenfilename()
col_list = ["X", "Y", "st_nm"]
csvfile = pd.read_csv(data, usecols=col_list)
pointLat = csvfile["X"]
pointLon = csvfile["Y"]

bit = int(input("Enter the number of bit:"))    
length = len(pointLat)+ 1

def selectionLat(x, y):
    midLat = []
    midLon = []
    for i in range(0, int((length)/bit)):
        j = i* bit
        sum_of_list = x[j] + x[j+(bit- 1)]
        sum_of_listi = y[j] + y[j+(bit- 1)]
        lat = sum_of_list/2
        lon = sum_of_listi/2    
        midLat.append(lat)
        midLon.append(lon)
    return midLat, midLon

la, lo = selectionLat(pointLat, pointLon)

data_gdf = gpd.GeoDataFrame(geometry = gpd.points_from_xy(la, lo))

ESRI_WKT = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'

data_gdf.to_file(filename='point1Com.shp', driver='ESRI Shapefile', crs= ESRI_WKT)

data_gdf.plot()
plt.show()
