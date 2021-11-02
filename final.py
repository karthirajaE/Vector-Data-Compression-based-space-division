from tkinter.filedialog import *
import pandas as pd
import geopandas as gpd



data = askopenfilename() #select point.csv
col_list = ["X", "Y", "st_nm"]
csvfile = pd.read_csv(data, usecols=col_list)
xpoint = csvfile["X"]
ypoint = csvfile["Y"]
plength = len(xpoint)
print("select grid file")


grid = askopenfilename() #select grid.csv
col_list1 = ["left", "right", "top", "bottom"]
gridfile = pd.read_csv(grid, usecols=col_list1)
left_point = gridfile["left"]
right_point = gridfile["right"]
top_point = gridfile["top"]
bottom_point = gridfile["bottom"] 
length_of_grid = len(left_point)


def Gridfilter(pointlength, gridlength, latitide, longitude, r, l, t, b):
    gridvalue = []
    midlon = []
    for i in range(0, int(pointlength)):
        lat = latitide[i]
        lon = longitude[i]
        j = 0
        while j < int(gridlength) :
            left = l[j]
            right = r[j]
            top = t[j]
            bottom = b[j]
            if left <= lat and right >= lat and top <= lon and bottom >= lon :
                
                mid1 = (right + left)/2
                mid2 = (top + bottom)/2
                #print(mid1,mid2)
                midlat.append(mid1)
                midlon.append(mid2)
                break
            else :
                j += 1

    return gridvalue 


gv = Gridfilter(plength, length_of_grid, xpoint, ypoint, right_point, left_point, top_point, bottom_point)




data_gdf = gpd.GeoDataFrame(geometry = gpd.points_from_xy(la, lo))

ESRI_WKT = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'

data_gdf.to_file(filename='filtered_clip005.shp', driver='ESRI Shapefile', crs= ESRI_WKT)
