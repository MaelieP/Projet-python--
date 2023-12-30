# Projet python ENSAE 
---
Lilou Soulas • Maëlie Perier

Ce projet est réalisé dans le cadre d'un cours de Python pour la data science de l'année 2023-2024

Ce projet est une étude sur les festivals en France et particulièrement sur leur emplacement en métropole. 
---
## Installation et utilisation 
Dans le notebook notebook.ipynb se trouvent les instructions détaillées pour installer les éléments requis et pour faire tourner le code. 

Le projet a pour objectif de faire une photographie des festivals en France (métropolitaine) en se concentrant surtout sur le lien qui pourrait unir les festivals à leur territoire. Ainsi, on cherche à avoir, d'une part une représentation visuelle de la répartition des festivals sur le territoire. D'autre part, on essaye de voir si le *type* de festival a un lien avec les données socio-démographiques de la commune dans laquelle il se déroule. 

Nous avons fait ce projet en utilisant Python 3.9.13 et nous vous conseillons d'en faire autant en exécutant le projet. 

---
## *Plan* 

I. Import et nettoyage des données 

II. Statistiques descriptives

III. Modélisation 

---



## I. Import et nettoyage des données 

On retrouvera dans le code AJOUTER LE FICHIER EXACT tous les détails relatifs à l'import et le netttoyage des données. L'essentiel est que nous avons importer à la fois une base de données "festivals" indiquant pour chaque festival crée en France depuis 1605, son nom, son année de création, sa discipline etc. D'autre part, nous avons merge cette base de données avec une base du recensement au niveau communal afin d'avoir la population par tranche d'âge et par PCS de chaque commune accueillant ou ayant accueilli un festival. 

## II. Statistiques descriptives

On fait des statistiques descriptives sur les communes, sur les festivals puis en croisant les deux. Plus précisément en regardant si la moyenne d'âge est plus élevée dans les communes accueillant des festivals de musique de type électronique plutôt que de musique classique etc. 

## III. Modélisation

On tente de modéliser notre problématique de deux manières différentes. D'une part, on représente grâce à une carte l'essor des festivals en France (notamment dans les années 2000-2010). Puis précisément, on essaye de voir si la carte des festivals est différente selon les types de festivals (musique, spectacle...). D'autre part, on fait des régressions logistiques multinomiales pour voir si l'âge et la PCS de la commune ont un effet sur le type de festival qui s'implante de la commune. Plus précisément on cherche à voir la probabilité qu'un festival soit de tel type plutôt que pluridisciplinaire en fonction de la tranche d'âge ou de la PCS majoritaire de la commune d'accueil. 


## Résultats 
Il semblerait qu'il y ait finalement peu de lien entre la nature d'un festival et les caractéristiques socio-démographiques de la commune dans laquelle il s'implante. Cette conclusion s'obtient tant à travers les cartes où l'on constate une similarité des cartes entre elles indépendamment des disciplines des festivals. Et d'autre part par les régressions qui ne semblent pas donner de résultats significatifs.  


### Extensions 

Peut-être serait-il plus pertinent de regarder à une échelle plus large ? Celle de la région ou du département car c'est à ces échelles là que l'on peut observer ou du moins interroger l'effet de politiques culturelles volontaristes sur l'implantation ou non de festivals. Un festival ne s'implante en effet jamais *au hasard*, cela dépend des accords avec les décideurs politiques locaux. 
Des données supplémentaires sur le soutien financier que peuvent apporter les politiques culturelles à certains festivals auraient enrichi l'analyse que nous tentons de mener à travers ce projet. 
