# WATIMIS - What Team Is?

Le projet que vous voyez ici est **WATIMIS (What team is?)**, une application pour PC qui permet d'identifier un club à partir d'une photo de son emblème/logo/blason. Il a pour utilité de simplifier la recherche en s'inspirant des outils de recherche à partir d'images (ex : Google Lens).

---

## Introduction

Ce projet est né d'un exercice scolaire. Plus exactement, étant en Licence d'informatique, le professeur du cours _"Infographie et Vision Informatique"_ nous a demandé un projet utilisant les différentes méthodes vues en cours ainsi qu'OpenCV.  
Il fallait utiliser la reconnaissance d'un motif dans une image. C'est ainsi que l'idée de **WATIMIS** est née.  

Cependant, l'énoncé nous obligeait à un mode d'utilisation simple dans le terminal, alors que WATIMIS avait pour vocation le **grand public**.  
La version développée que vous voyez aujourd'hui est une version améliorée de ce projet scolaire, absolument pas obligatoire mais née de l'idée d'aller au bout des choses.

---

## Notice d'Utilisation

Pour utiliser **WATIMIS** :
1. Ouvrez l'application.
2. Cliquez sur **"Sélectionner une photo"** et choisissez une image prise au préalable.
3. Cliquez sur **"Continuer"**.

### Résultat :
- En grand, vous verrez le club correspondant à votre image, avec les correspondances tracées.
- À droite, une liste des clubs potentiellement identifiés est affichée (en cas d'erreurs, les clubs avec des fortes correspondances sont suggérés).

---

## Fonctionnement Technique

La méthode utilisée est basée sur les techniques enseignées en cours, en particulier **ORB (Oriented FAST and Rotated BRIEF)** :
1. L'image est téléchargée et convertie en niveaux de gris.
2. **ORB** détecte les principales variations d'intensité comme points clés et sélectionne les meilleurs.
3. Après avoir détecté les points clés des deux images comparées, le programme recherche les correspondances entre ces points.
4. Le programme compte les "bons matches" pour identifier l'image la plus proche et en conclure que le logo correspond à celui sur l'image donnée par l'utilisateur.

---

## Fiabilité

Cette méthode a été améliorée avec l'usage de la fonction **FLANN** pour fiabiliser l'algorithme.  
Malgré tout, elle reste limitée. Voici un test réalisé avec :
- **5 logos de référence**  
- **50 images à tester**

### Résultats :
- **86% de résultats positifs** : 
  - 62% des cas où le résultat principal était correct.
  - 24% des cas où le résultat correct était suggéré parmi les possibilités.

### Limites :
1. Les images prises de loin ou dont le logo est mal défini.
2. Le logo de l'équipe de France est le plus difficile à détecter.

---

## Structure du Projet

- **`main.py`** : Le point d'entrée principal.
- **Images de référence** : Base de données pour la comparaison.
- **Fichier de test** : Script permettant de tester la fiabilité avec un jeu de données.

---

