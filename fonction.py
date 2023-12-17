import pandas as pd
import requests
import geopandas as gpd
import matplotlib.pyplot as plt
import pyproj


#------------------------------------------LECTURE DE FICHIER-------------------------------------------

#Transforme le fichier en 1 fichier markdown qui s'affiche bien sur vscode.
def into_md(data, nom):
    # Charger le fichier CSV

    # Convertir le DataFrame en Markdown
    markdown = data.to_markdown()

    # Écrire le résultat dans un fichier Markdown
    chemin_md = f'C:/Users/lilou/Documents/Backup Lilou 20220527/Bureau/IMPORTANT/ENSAE/PYTHON CROUS/{nom}.md'
    with open(chemin_md, 'w', encoding='utf-8') as fichier_md:
        fichier_md.write(markdown)

    return



#Donne la ligne numéro "ligne" d'un dataframe sous forme de liste
def ligne(numero_ligne, data):

    if not data.empty:
        ligne = data.iloc[0].tolist()
        return(ligne)
    else:
        return(0)

#Donne la premiere ligne d'un dataframe, cad les noms des différentes colonnes sous forme de liste
def nom_de_colonne(data):

    if not data.empty:
        colonnes = data.columns.tolist()
        return(colonnes)
    else:
        return(0)
    
# Lit un fichier à partir d'un chemin menant à un fichier 
def lecture_fichier(nom, extension):
    if extension == "csv":

        if nom=="festival" :
            chemin = "C:/Users/lilou/Documents/Backup Lilou 20220527/Bureau/IMPORTANT/ENSAE/PYTHON CROUS/festivals-global-festivals-_-pl.csv"
        if nom=="panorama" :
            chemin = "C:/Users/lilou/Documents/Backup Lilou 20220527/Bureau/IMPORTANT/ENSAE/PYTHON CROUS/panorama-des-festivals.csv"
        
        fichier=pd.read_csv(chemin, sep=";")

    if extension == "shp":
        if nom=="festival" :
            chemin = "C:/Users/lilou/Documents/Backup Lilou 20220527/Bureau/IMPORTANT/ENSAE/PYTHON CROUS/festivals-global-festivals/festivals-global-festivals-_-pl.shp"
        if nom=="carte"  :
            chemin = "C:/Users/lilou/Documents/Backup Lilou 20220527/Bureau/IMPORTANT/ENSAE/PYTHON CROUS/fond_carte/regions_2015_metropole_region.shp"
        if nom=="carte_academie":
            chemin = "C:/Users/lilou/Documents/Backup Lilou 20220527/Bureau/IMPORTANT/ENSAE/PYTHON CROUS/fond_carte_academies/academies-20160209.shp"
        if nom=="carte_region":
            chemin = "C:/Users/lilou/Documents/Backup Lilou 20220527/Bureau/IMPORTANT/ENSAE/PYTHON CROUS/fond_carte_region/regions-20180101.shp"

        fichier = gpd.read_file(chemin)


    return fichier

'''
url et chemin des fichiers
url_fest_evid = "https://www.data.gouv.fr/fr/datasets/liste-des-festivals-en-france/#/resources/47ac11c2-8a00-46a7-9fa8-9b802643f975"
url_fest = "https://data.culture.gouv.fr/explore/dataset/festivals-global-festivals-_-pl/download?format=csv&timezone=Europe/Berlin&use_labels_for_header=false"
url_fest_stable = "https://www.data.gouv.fr/fr/datasets/r/47ac11c2-8a00-46a7-9fa8-9b802643f975"
chemin_fichier_fest = "C:/Users/lilou/Documents/Backup Lilou 20220527/Bureau/IMPORTANT/ENSAE/PYTHON CROUS/festivals-global-festivals-_-pl.csv"
chemin_fichier_fdcarte = "C:/Users/lilou/Documents/Backup Lilou 20220527/Bureau/IMPORTANT/ENSAE/PYTHON CROUS/fond_carte/regions_2015_metropole_region.shp"
chemin_fichier_fest_sh = "C:/Users/lilou/Documents/Backup Lilou 20220527/Bureau/IMPORTANT/ENSAE/PYTHON CROUS/festivals-global-festivals/festivals-global-festivals-_-pl.shp"
chemin_fichier_pano = "C:/Users/lilou/Documents/Backup Lilou 20220527/Bureau/IMPORTANT/ENSAE/PYTHON CROUS/panorama-des-festivals.csv"
'''





#-------------------------------------CARTE-------------------------------------------

def carte_fest_marche(emplacements_festivals):
    
    # Charger le fond de carte de la France
    fond_de_carte = lecture_fichier("carte_academie", "shp")

    #On définit un crs commun - rapport au fait de lire une carte ou non
    fond_de_carte = fond_de_carte.set_crs(epsg=4326)
    emplacements_festivals = emplacements_festivals.set_crs(epsg=4326)  # Assurez-vous d'ajuster le CRS ici
   
    #On vérifie que les deux crs sont les mêmes - on affiche les résultats
    print("CRS fond_de_carte =", fond_de_carte.crs)
    print("CRS emplacements_festivals =", emplacements_festivals.crs)

    print(fond_de_carte.head())
    print(emplacements_festivals.head())


    # Créer une figure matplotlib
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Afficher le fond de carte
    fond_de_carte.plot(ax=ax, color='lightgray', edgecolor='black')

    # Afficher les emplacements des festivals
    emplacements_festivals.plot(ax=ax, color='red', marker='o', markersize=5)

    # Ajouter un titre à la carte
    plt.title('Carte des Festivals en France')

    # Afficher la carte
    plt.show()

    return





#Creer une carte des emplacements des festivales en France. En argument: le nom du fichier choisit, ici "festival"
def carte_fest(emplacements_festivals, fond_de_carte):
    
    #On vérifie que les deux crs sont les mêmes - on affiche les résultats
    print(fond_de_carte.crs)
    print(emplacements_festivals.crs)

    # Créer une figure matplotlib
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Afficher le fond de carte
    fond_de_carte.plot(ax=ax, color='lightgray', edgecolor='black')

    # Afficher les emplacements des festivals
    emplacements_festivals.plot(ax=ax, color='red', marker='o', markersize=5)

    # Ajouter un titre à la carte
    plt.title('Carte des Festivals en France')

    # Afficher la carte
    plt.show()

    return

#Tente de débuguer la fonction d'avant en affichant cote a cote le fond de carte et les emplacements
def carte_fest_debug(emplacements_festivals):

    # Charger le fond de carte de la France
    fond_de_carte = lecture_fichier("carte", "shp")

    
    print(emplacements_festivals.crs)
    print(fond_de_carte.crs)

    # On définit un crs commun - rapport au fait de lire une carte ou non
    fond_de_carte = fond_de_carte.set_crs(epsg=4326)
    emplacements_festivals = emplacements_festivals.set_crs(epsg=4326)  # Assurez-vous d'ajuster le CRS ici
   

    # On vérifie que les deux CRS sont les mêmes - on affiche les résultats
    print(fond_de_carte.crs)
    print(emplacements_festivals.crs)


    #emplacements_festivals = emplacements_festivals.set_crs(epsg=4326)  # Assurez-vous d'ajuster le CRS ici

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))


    # Premier sous-plot : fond de carte
    fond_de_carte.plot(ax=axs[0], color='lightgray', edgecolor='black')
    axs[0].set_title('Fond de carte de la France')

    # Deuxième sous-plot : emplacements des festivals
    emplacements_festivals.plot(ax=axs[1], color='red', marker='o', markersize=5)
    axs[1].set_title('Emplacements des Festivals')

    # Ajuster la disposition pour éviter les chevauchements
    plt.tight_layout()

    plt.show()



    return

def data_1_an(data, annee):

    datacop = data.copy()

    #On convertit en numérique et remplace toutes les valeurs qui ne sotn aps numériques par des Nan
    datacop['annee_de_cr'] = pd.to_numeric(datacop['annee_de_cr'], errors='coerce')
    
    # On enlève toutes les lignes dont la valeur de la colonne 'code_insee_commune' est NaN
    datacop = datacop.dropna(subset=['annee_de_cr'])

    # On garde les lignes qui correspondent à la bonne année
    data_annee = datacop[datacop['annee_de_cr'] == annee]

    return data_annee


#contient la conversion en numeric
def carte_1_an(emplacements_festivals, fond_de_carte, annee):

    #On convertit en numérique et remplace toutes les valeurs qui ne sotn aps numériques par des Nan
    emplacements_festivals['annee_de_cr'] = pd.to_numeric(emplacements_festivals['annee_de_cr'], errors='coerce')
    
    # On enlève toutes les lignes dont la valeur de la colonne 'code_insee_commune' est NaN
    emplacements_festivals = emplacements_festivals.dropna(subset=['annee_de_cr'])

    # On enlève les lignes dont la date de créa est diff de celle donnée en argument
    emplacements_festivals = emplacements_festivals[emplacements_festivals['annee_de_cr'] == annee]

    into_md(emplacements_festivals, "test")

    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Afficher le fond de carte
    fond_de_carte.plot(ax=ax, color='lightgray', edgecolor='black')

    # Afficher les emplacements des festivals
    emplacements_festivals.plot(ax=ax, color='red', marker='o', markersize=5)

    # Ajouter un titre à la carte
    plt.title(f'Carte des Festivals en France créés en {annee}')

    # Afficher la carte
    plt.show()
    #plt.close(fig)

    return

#ne contient pas la conversion en numeric ni le drop na
#Renvoi une carte de la France vide si aucuns festival n'a été créé l'année demandée
def carte_1_an_bis(emplacements_festivals, fond_de_carte, annee):
    # On enlève toutes les lignes dont la valeur de la colonne 'code_insee_commune' est NaN

    # On enlève les lignes dont la date de création est différente de celle donnée en argument
    emplacements_festivals = emplacements_festivals[emplacements_festivals['annee_de_cr'] == annee]

    if not emplacements_festivals.empty:
        fig, ax = plt.subplots(figsize=(12, 6))

        # Afficher le fond de carte
        fond_de_carte.plot(ax=ax, color='lightgray', edgecolor='black')

        # Afficher les emplacements des festivals
        emplacements_festivals.plot(ax=ax, color='red', marker='o', markersize=5)

        # Ajouter un titre à la carte
        plt.title(f'Carte des Festivals en France créés en {annee}')

        # Afficher la carte
        plt.show()

        return

    # Si aucuns festivals n'ont été créés cette année, afficher seulement le fond de carte
    fig, ax = plt.subplots(figsize=(12, 6))
    fond_de_carte.plot(ax=ax, color='lightgray', edgecolor='black')
    plt.title(f'Aucun festival créé en France en {annee}')
    plt.show()
    return

#Génere le fond de carte tout seul
def make_fond_carte(fond_de_carte):
    fig, ax = plt.subplots(figsize=(12, 6))
    fond_de_carte.plot(ax=ax, color='lightgray', edgecolor='black')
    return fig, ax

#Génere une carte de la france avec les emplacements des festivals 
def carte_1_an_rapide(emplacements_festivals, ax, annee):
    # Cette fonction marche si on a déja convertit les valeurs en numérique et remplacé toutes les valeurs qui ne sont pas numériques par des NaN

    # On enlève les lignes dont la date de création est différente de celle donnée en argument
    emplacements = emplacements_festivals[emplacements_festivals['annee_de_cr'] == annee]

    # On affiche les emplacements des festivals
    layer = emplacements.plot(ax=ax, color='red', marker='o', markersize=5)

    # On affiche un titre à la carte
    # plt.title(f'Carte des Festivals en France créés en {annee}')

    # On affiche la carte
    return layer


#Enlève du dataframe les festivals hors france métropolitaine
def festi_sans_dom(data):

    #On copie notre fichier original pour ne pas l'abimer
    datacop = data.copy()

    #On garde seulement les colonnes qui nous interessent
    datacop = datacop[['nom_du_festival', 'code_insee_commune', 'decennie_de_creation_du_festival', 'annee_de_creation_du_festival', 'identifiant', 'geocodage_xy', 'identifiant_cnm']]

    #On enlève toutes les lignes dont la valeur de la colonne 'code_insee_commune' est Nan
    data_sans_nan = datacop.dropna(subset=['code_insee_commune'])

    #On convertit la colonne des codes insee en str pour pouvoir ensuite les comparer avec le seuil de 97000 et les codes de la corse qui commencent par 2A ou 2B
    data_sans_nan['code_insee_commune'] = data_sans_nan['code_insee_commune'].astype(str)

    #On print les infos de la base initiale:
    print("avant le loc. nb de ligne =", len(data_sans_nan))

    #On enlève les lignes dont la valeur de code_insee_commune est domtom
    data_sans_dom = data_sans_nan[data_sans_nan['code_insee_commune'].apply(lambda x: x.startswith('2A') or x.startswith('2B') or int(x) < 97000)]


    #On affiche les infos du dataframe après la loc:
    print("après le loc. nb de ligne =", len(data_sans_dom))

    return data_sans_dom

#Prend un fichier shapefile des emplacements de festivak et enlèves les colonnes non necessaires, ainsi que les lognes correspondant aux domtom
def festi_sans_dom_shapefile(gdf):

    #On garde seulement les colonnes qui nous intéressent
    colonnes_interessantes = ['nom_du_fest', 'code_postal','code_insee_', 'decennie_de', 'annee_de_cr', 'identifiant', 'geometry']
    gdf = gdf[colonnes_interessantes]

    #On convertit en numérique et remplace toutes les valeurs qui ne sotn aps numériques par des Nan
    gdf['code_postal'] = pd.to_numeric(gdf['code_postal'], errors='coerce')
    
    # On enlève toutes les lignes dont la valeur de la colonne 'code_insee_commune' est NaN
    gdf = gdf.dropna(subset=['code_postal'])

    # On affiche les infos du DataFrame avant la condition
    #print("Avant la condition, nombre de lignes =", len(gdf))

    # On enlève les lignes dont le code postal est inférieur à 97000 (code postal des dom-tom)
    gdf_sans_dom = gdf[gdf['code_postal'] < 97000]

    # On affiche les infos du DataFrame après la condition
    #print("Après la condition, nombre de lignes =", len(gdf_sans_dom))

    return gdf_sans_dom

def academie_sans_dom(data):
    data = data.drop([10, 11, 12, 13])
    # Réindexer le DataFrame après la suppression des lignes
    data = data.reset_index(drop=True)

    #Truc chelou: st pierre et miquelon est rattaché à l'académie de Caen, on cherche à l'enlever

    return data

def region_sans_dom(data):
    data = data.drop([0, 2, 7, 11, 13])
    # Réindexer le DataFrame après la suppression des lignes
    data = data.reset_index(drop=True)

    #Truc chelou: st pierre et miquelon est rattaché à l'académie de Caen, on cherche à l'enlever

    return data





#-----------------------------------------HISTOGRAMME-----------------------------------------------

#Construit un histogramme du nombre de festival créés par année pour le fichier festival
def hist_date_festi(data):
    
    #On extrait la colonne date de création
    date_creation = data['annee_de_creation_du_festival']
    print(date_creation)

    #attention, ici on enlève juste les NaN. 
    date_creation = pd.to_datetime(date_creation, errors='coerce')

    #On creer un histogramme avec le nombre de creation de festival en fonction du temps
    plt.hist(date_creation, bins=70, edgecolor='black', alpha=0.7)
    plt.xlabel('Dates')
    plt.ylabel('Fréquence')
    plt.title('Date de création du festival pour le fichier "festival"')

    # Afficher l'histogramme
    plt.show()
    return

#Construit un histogramme du nombre de festival créés par année pour le fichier panorama
def hist_date_pano(data):

    #On extrait la colonne date de création
    date_creation = data['date_de_creation']
    print(date_creation)

    #On creer un histogramme avec le nombre de creation de festival en fonction du temps
    date_creation = pd.to_datetime(date_creation)

    # Créer un histogramme à partir de la colonne 'dates'
    plt.hist(date_creation, bins=70, edgecolor='black', alpha=0.7)
    plt.xlabel('Dates')
    plt.ylabel('Fréquence')
    plt.title('Date de création du festival pour le fichier "panorama')

    # Afficher l'histogramme
    plt.show()
    return


'''

#Répare la colonne date de création du dataframe festival - EN COURS DE CONSTRUCTION
def reparation_date(data):
    date_creation = data['annee_de_creation_du_festival']
    print(date_creation)

#on récup les dates
date_creation = festi['annee_de_creation_du_festival']
print(date_creation)

# on parcours les dates


# Vérifier si les éléments de la colonne 'Date' ont la forme d'une année à 4 chiffres
dates_valides = date_creation.astype(str).str.match(r'^\d{4}$') | date_creation.isna()
dates_non_valides = ~date_creation.astype(str).str.match(r'^\d{4}$')

print(dates_valides)

# Afficher les lignes où la condition est vraie
resultat = festi[dates_non_valides]
print(resultat)

into_md(resultat)


    return

'''






