
Introduction:

Le projet que vous voyez ici est WATIMIS (What team is?), une application pour PC qui permet d'identifier un club à partir
d'une photo de son emblème/logo/blason. Elle a pour utilité de simplifier la recherche en s'inspirant des outils de recherches
à partir d'images (ex: Google Lens).

Ce projet est né d'un exercice scolaire. Plus exactement, étant en Licence d'informatique, le professeur du cours
"Infographie et Vision Informatique" nous a demandé un projet utilisant les différentes méthodes vues en cours ainsi qu'OpenCV.
Il fallait utiliser la reconnaissance d'un motif dans une image. C'est ainsi que l'idée de WATIMIS est née. Cependant,
l'énoncé nous obligeait à un mode d'utilisation simple dans le terminal, or, WATIMIS avait pour vocation le grand public.
La version développée que vous voyez aujourd'hui n'est ni plus ni moins qu'une version améliorée de ce projet scolaire,
absolument pas obligatoire mais née de l'idée d'aller au bout des choses.

************************************************NOTICE D'UTILISATION****************************************************

Pour utiliser WATIMIS, il suffit d'ouvrir l'application, d'appuyer sur "sélectionner une photo" et de choisir une photo 
prise au préalable. Pour finir, appuyez sur le bouton "continuer", et c'est tout. Avec l'image donnée, le programme va alors 
effectuer une comparaison entre votre image et toutes celles de son jeu de données, puis il vous donnera le verdict.

Les résultats sont simples à comprendre : en grand est affiché le club correspondant (avec les correspondances tracées), 
avec à droite la liste des potentiels clubs identifiés. L'algorithme pouvant se tromper, il suggère donc des clubs avec une forte correspondance.

**************************************************************************************************************************

Fonctionnement:

Il faut savoir que la liberté de la méthode utilisée était restreinte. Je devais me baser sur des techniques enseignées en cours
et utilisées en TD (voir le dossier dédié). WATIMIS se base donc sur l'ORB (Oriented FAST and Rotated BRIEF) :
L'image est téléchargée, convertie en niveaux de gris, puis l'ORB détecte les principales variations d'intensités et les déclare 
comme des points clés dont il va alors garder les meilleurs. Enfin, après avoir effectué ceci sur les deux images comparées, il va 
rechercher les points clés similaires dans chaque image et réaliser des "matches" entre eux. Enfin, il comptera le nombre de "bons matches" 
qui permettront d'établir quelle image en a le plus et ainsi conclure que ce logo correspond à celui sur l'image donnée par l'utilisateur.

Fiabilité:

Cette méthode a été améliorée par mes soins avec l'usage de la fonction FLANN afin de fiabiliser l'algorithme. Cependant, malgré tout, 
cette technique demeure peu fiable. Dans le dossier contenant le rendu de cours, il y a un fichier `.py` permettant d'effectuer un test
massif du programme avec 5 logos de référence et un jeu de données de 50 images. Après l'avoir lancé, j'ai obtenu 86% de résultats positifs
(62% des cas où le résultat principal était le bon, 24% où le résultat était suggéré dans les possibilités). On peut ainsi voir quelles
images n'ont pas très bien fonctionné :
1. Les images prises de loin où le logo du club n'est pas très bien tracé.
2. Le logo de l'équipe de France semble être le plus difficile à détecter.
"""


