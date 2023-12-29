import pandas as pd
import requests
import pyproj
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mapclassify import NaturalBreaks

from fonction import ligne, nom_de_colonne, carte_1_an_rapide, carte_1_an, carte_1_an_bis, region_sans_dom, academie_sans_dom, carte_fest_marche, lecture_fichier, data_1_an, carte_fest, hist_date_festi, hist_date_pano, into_md, carte_fest_debug, festi_sans_dom, festi_sans_dom_shapefile


#Lecture du fichier voulu
festi = lecture_fichier("festival", "csv")
shp_festi = lecture_fichier("festival", "shp")
fond_de_carte = lecture_fichier("carte_region", "shp")


#convertit le fichier shp complet en un fichier sans dom tom
shp_sans_dom = festi_sans_dom_shapefile(shp_festi)
reg_sans_dom = region_sans_dom(fond_de_carte)

#On affiche le graphe de tous les emplacements de festival en France
#carte_fest(shp_sans_dom, reg_sans_dom)

#On affiche les festivals crés l'année X
shp_sans_dom['annee_de_cr'] = pd.to_numeric(shp_sans_dom['annee_de_cr'], errors='coerce')
carte_1_an_bis(shp_sans_dom, reg_sans_dom, 2001)

plt.plot(reg_sans_dom)



