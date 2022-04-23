"""
Created on Wed Apr 2022

@author: Kimia Chenary (kimia.chenaari@gmail.com)
"""

#import necessary Python Libraries
import csv 
import osmnx as ox
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Getting the data from OSMnx 
ox.config(use_cache=True, log_console=True)
G = ox.graph_from_place('District 1, Mashhad, Iran', network_type='drive')
G = ox.add_edge_bearings(G)
print(G)
gdf_edges = ox.graph_to_gdfs(G, nodes=True)
df = pd.DataFrame(gdf_edges)
  
#Visualizing
bearings=df['bearing']
ax = bearings.hist(bins=30, zorder=2, alpha=0.8)
xlim = ax.set_xlim(0, 360)
ax.set_title('Network Edge Bearings of (Samen District, Mashhad, Iran)')
plt.show()

n = 30
count, division = np.histogram(bearings, bins=[ang*360/n for ang in range(0,n+1)])
division = division[0:-1]
width =  2 * np.pi/n
ax = plt.subplot(111, projection='polar')
ax.set_theta_zero_location('N')
ax.set_theta_direction('clockwise')
bars = ax.bar(division * np.pi/180 - width * 0.5 , count, width=width, bottom=0.0)
ax.set_title('Network Edge Bearings of (Samen District, Mashhad, Iran)', y=1.1 )
plt.show()