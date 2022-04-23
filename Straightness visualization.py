"""
(G-mail: kimia.chenaari@gmail.com)
"""

"""

Street Straightness-centrality Visualization Using Momepy library. for more information visit http://docs.momepy.org/.

"""
#import necessary Python Libraries
import geopandas as gpd
import momepy
import osmnx as ox
import matplotlib.pyplot as plt
import matplotlib as mpl
import contextily
from matplotlib_scalebar.scalebar import ScaleBar
import osmnx as ox

#Getting the region of interest's data from OSMnx 
streets_graph = ox.graph_from_place('District 11, Mashhad, Iran', network_type='drive')
streets_graph = ox.projection.project_graph(streets_graph)

streets = ox.graph_to_gdfs(ox.get_undirected(streets_graph), nodes=False, edges=True,
                                   node_geometry=False, fill_edge_geometry=True)

edges = ox.graph_to_gdfs(ox.get_undirected(streets_graph), nodes=False, edges=True,
                                   node_geometry=False, fill_edge_geometry=True)

#Visualizing
f, ax = plt.subplots(figsize=(5, 5))
edges.plot(ax=ax, linewidth=0.2)
ax.set_axis_off()


primal = momepy.gdf_to_nx(edges, approach='primal')

primal = momepy.straightness_centrality(primal)

nodes = momepy.nx_to_gdf(primal, lines=False)
f, ax = plt.subplots(figsize=(15, 15))
nodes.plot(ax=ax, column='straightness', cmap='Spectral_r', scheme='quantiles', k=15, alpha=0.6)
ax.set_axis_off()
ax.set_title('straightness')
plt.show()

ax = nodes.plot(
    "straightness", 
    scheme="fisherjenkssampled",
    markersize=0.5,
    legend=True,
    figsize=(12, 12),

    
)

#Adding basemap 
contextily.add_basemap(
    ax,
    crs=nodes.crs,
    source=contextily.providers.CartoDB.DarkMatterNoLabels
)

#Adding scalebar
scalebar = ScaleBar(
    1,
    box_alpha=0,
    location="lower right",
    color='white',
    length_fraction=0.25,
    font_properties={"size": 12},
)
ax.add_artist(scalebar)
ax.set_title("straightness");
