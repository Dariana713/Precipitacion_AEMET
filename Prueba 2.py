# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:56:52 2022

@author: diavivel
"""
import netCDF4 as nc 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Malla de puntos (x,y) csv de precipitación de Requena Utiel
df = pd.read_csv(r'C:\Users\juacaran\Desktop\Dariana/Red_AEMET_SPAIN.csv')
print(df)

# Malla de puntos (x,y) csv de precipitación de CHJ
col_names = ['no','x','y','dato']
dfchj = pd.read_csv(r'C:\Users\juacaran\Desktop\Dariana/Malla_CHJ.csv', names=col_names, header=1)
#informacion
aa=dfchj.head()  
bb=dfchj.shape
#sacar valors
no=dfchj['no']
Numero_no=no[0]

print(no)
len_=len(dfchj)
for Ud in range(len_):
    print(no[Ud])

# dfr <- as.data.frame('df' , xy=TRUE)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#Cargando los datos de Precipitación de toda  España  a 5km año 2019 (AEMET) archivo netCDF.
# precipitacion = "Datos de precipitación requena utiel buena"
# #map_data = gpd.read_file(precipitacion)
# #map_data.head()

# #Extrayendo los datos de precipitación solo de Requena Utiel
# data = nc.extract_grid_timeseries("None", 'sfcanXXXX0101aXXXX1231_rot_mask.nc', 'df', 'precipitation', 'AEMET', [2019,2019], 'daily')
# print(data)
# plt.plot(data['precipitation'].values)

# #--------------------------------------------------------------------------------------------------------------------------------------------------------
# #Guardar los datos en un csv
# data.to_csv("PrecipitacionRequena2019.csv", index=False, sep=";")

# #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# #Otra forma
# #Extrayendo los datos de precipitación solo de Requena Utiel
# PrecipitacionRequena2019 = nc.extract_grid_timeseries("None", 'sfcanXXXX0101aXXXX1231_rot_mask.nc', 'df', 'precipitation', 'AEMET', [2019,2019], 'daily')
# print(data)
# plt.plot(data['precipitation'].values)

# #--------------------------------------------------------------------------------------------------------------------------------------------------------
# #Guardar los datos en un csv
# data.to_csv("PrecipitacionRequena2019.csv", index=False, sep=";")