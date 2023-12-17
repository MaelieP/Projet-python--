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



'''
#------------------------------------------------TEST D'ANIMATION--------------------------
print("teeeeeeest", shp_sans_dom['annee_de_cr'].dtype)

# Chargement du fond de carte de la France (assurez-vous d'avoir le fichier correspondant)
france_map = reg_sans_dom

shp_sans_dom['annee_de_cr'] = pd.to_datetime(shp_sans_dom['annee_de_cr'], errors='coerce')
shp_sans_dom = shp_sans_dom.dropna(subset=['annee_de_cr'])

# Définir le nombre total d'années pour l'animation
annee_max = shp_sans_dom['annee_de_cr'].dt.year.max()
annee_min = shp_sans_dom['annee_de_cr'].dt.year.min()
total_years = annee_max - annee_min + 1
print("total_years=", total_years)


for i in range(annee_min, annee_max, 1):
    print("i=", i)
    carte_1_an_bis(shp_sans_dom, reg_sans_dom, i)


carte_1_an_bis(shp_sans_dom, reg_sans_dom, 2011)


# Création de la figure et de l'axe initial
fig, ax = plt.subplots(figsize=(8, 6))
france_map.boundary.plot(ax=ax)

def update(frame):
    print("frame", frame)
    ax.clear()
    france_map.boundary.plot(ax=ax)
    
    # Appeler votre fonction existante pour afficher la carte pour une année spécifique
    carte_1_an_bis(shp_sans_dom, france_map, shp_sans_dom['annee_de_cr'].dt.year.min() + frame)
    #ax.set_aspect('equal')

# Création de l'animation
animation = FuncAnimation(fig, update, frames=total_years, repeat=False)

# Afficher l'animation
plt.show()


'''
