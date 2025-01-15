
### Introduction :  

Le projet que vous voyez ici est **WATIMIS** (*What team is?*), une application pour PC qui permet d'identifier un club 
à partir d'une photo de son emblème/logo/blason. Elle a pour utilité de simplifier la recherche, en s'inspirant des outils de recherche 
à partir d'images (ex. : Google Lens).  

Ce projet est né d'un exercice scolaire. Plus précisément, dans le cadre de ma Licence en informatique, notre professeur du cours "Infographie et Vision Informatique" 
nous a demandé de réaliser un projet utilisant les différentes méthodes vues en cours ainsi qu'OpenCV. L'objectif était d'utiliser la reconnaissance d'un motif dans une image. 
C'est ainsi que l'idée de **WATIMIS** a vu le jour. Cependant, l'énoncé imposait un mode d'utilisation simple dans le terminal.
Or, WATIMIS avait pour vocation de s'adresser au grand public.  

La version développée que vous voyez aujourd'hui est une version améliorée de ce projet scolaire, non obligatoire mais réalisée dans l'idée d'aller au bout des choses.  

---

*******Notice d'utilisation :****************************************************************************************************************************************************
*                                                                                                                                                                               *
*  Pour utiliser **WATIMIS**, il suffit d'ouvrir l'application, d'appuyer sur "Sélectionner une photo", puis de choisir une photo prise au préalable.                           *
*  Enfin, appuyez sur le bouton "Continuer", et c'est tout.                                                                                                                     * 
*                                                                                                                                                                               *
*  Avec l'image donnée, le programme va effectuer une comparaison entre votre image et toutes celles de son jeu de données, pour ensuite vous fournir un verdict.               *
*                                                                                                                                                                               *
*  Les résultats sont simples à comprendre :                                                                                                                                    *
*  - En grand s’affiche le club correspondant (avec les correspondances tracées).                                                                                               *
*  - Sur la droite, une liste des clubs potentiels identifiés est proposée. L'algorithme pouvant se tromper, il suggère donc des clubs présentant de fortes                     *
*   correspondances.                                                                                                                                                            *
*                                                                                                                                                                               *                                                                                                                                                                                                               *
*********************************************************************************************************************************************************************************
---

### ***Fonctionnement :***  

Il est important de noter que la méthode utilisée était restreinte par les consignes : je devais me baser sur des techniques enseignées en cours et utilisées 
en travaux dirigés (voir le dossier dédié).  

**WATIMIS** repose donc sur l’algorithme **ORB** (*Oriented FAST and Rotated BRIEF*).  
1. L’image est téléchargée, puis convertie en niveaux de gris.  
2. ORB détecte les principales variations d’intensité et les déclare comme points-clés, en gardant les meilleurs.  
3. Après avoir réalisé cette opération sur les deux images comparées, l'algorithme recherche les points-clés similaires entre elles et établit des "matches".  
4. Enfin, il compte le nombre de "bons matches", ce qui permet de déterminer quelle image a le plus de correspondances et ainsi de conclure que ce logo correspond
   à celui fourni par l’utilisateur.  

---

### ***Fiabilité :***  

Cette méthode a été améliorée grâce à l’utilisation de la fonction **FLANN**, ce qui a permis de fiabiliser l’algorithme. Cependant, malgré ces améliorations, la méthode reste imparfaite.  

Dans le dossier contenant le rendu de cours, un fichier `.py` permet d’effectuer un test massif du programme avec 5 logos de référence et un jeu de données de 50 images. Après l’avoir lancé,
j’ai obtenu **86 % de résultats positifs** :  
- 62 % des cas où le résultat principal était correct.  
- 24 % des cas où le bon résultat figurait parmi les suggestions.  

Les limites observées sont les suivantes :  
1. Les images prises de loin, où le logo du club est mal défini.  
2. Le logo de l’équipe de France semble être le plus difficile à détecter.
