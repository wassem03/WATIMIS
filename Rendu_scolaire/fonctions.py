#Fichier comprenant toutes les fonctions nécessaire au bon fonctionnement du programme
#!!!Pour faire fonctionner le programme, veuillez lancer le main (ou le large_test pour obtenir un test de tout le jeu de données)

#######################################################################################

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

######################################################################################

def liste_fichiers(dossier):                                            #Création de la fonction permettant de donner une liste contenant le nom de tout les fichiers d'un dossier
    fichiers = []
    for fichier in os.listdir(dossier):
        if os.path.isfile(os.path.join(dossier, fichier)):              #Vérification si le dossier comporte un fichier
            fichiers.append(fichier)                                    #Ajout du nom du fichier dans une liste prévue a cet effet
                                                                        
    return fichiers                                                     #Revoie la liste contenant les fichiers présents dans le dossier
 
def redimensionner(image):                                              #Fonction de rendimensionnement
    height, width = image.shape[:2]                                     #La fonction a été crée mais pas utilisée car elle en déformant les images, on perdait en fiabilité
    if height > 800 or width > 800:
        height, width = height//2,width//2
        return cv2.resize(image,(int(height),int(width)),interpolation=cv2.INTER_AREA)
    else:
        return image


def comparaison(nom_image,nom_logo,choix):                              #Creation de la fonction principale qui effectue la comparaison des images entres elles grace à la methode ORB
                                                                        #Cette fonction prend en compte l'image, un logo, et un choix binaire qui sera expliquer ensuite    
    image = cv2.imread(nom_image, cv2.IMREAD_COLOR)
    logo = cv2.imread(nom_logo, cv2.IMREAD_COLOR)                       #Lecture des images
   
    image_gray =  cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)                  #Conversion en niveau de Gris

    orb = cv2.ORB_create()                                              #Création de l'orb
    keypoints_logo, descriptors_logo = orb.detectAndCompute(logo_gray, None)    #Détection des points d'intérêts (Keypoints) et des descripteur
    keypoints_image, descriptors_image = orb.detectAndCompute(image_gray, None)


    ##########################################################

    #Cette partie n'a pas été vue dans le cours, il s'agit la d'un ajout que nous avions effectué afin de fiabiliser le programme (méthodes validées par notre professeur)
    #Ici, on crée un dictionnaires comportant les paramètres nécessaires au bon fonctionnement de la fonction FLANN "Fast Library for Approximate Nearest Neighbors"

    index_params = {                                                    
        "algorithm":6,                                                  #On utilise ici l'algorithme n°6 LSH  (Locality Sensitive Hashing), selon nos recherches, il sera le plus approprié                                        
        "table_number":6,                                               #On définit le nombre de table de Hachage utilsé
        "key_size":12,                                                  #On définit la taille des clés de la table de hachage
        "multi_probe_level":1                                           #Parametre binaire necessaire pour obtenir une recherche rapide
    }

    search_params = {"checks":50}                                       #On définit ici le nombre vérification pour chaque correspondance, 50 étant logiquement suffisant pour une assez bonne précision
    flann = cv2.FlannBasedMatcher(index_params, search_params)          #On initialise l'objet permettant de faire les correspondances entres les descripteurs

    ##########################################################

    matches = flann.knnMatch(descriptors_logo, descriptors_image,k=2)   #Creation des matches entre les descripteurs du logo et de l'image

    
    good_matches = []                                                   #Récupération uniquement des bons matche
    for match in matches:
        if len(match) == 2:                                             #Vérifier qu'il y a deux correspondances
            m, n = match
            if m.distance < 0.7 * n.distance:                           #Seul la distance des points ORB de plus de 0.7 seront retenu (le min = 0 et le max = 1)
                good_matches.append(m)     

    if choix == 0:                                                      #La fonction prend en compte un choix, si on met 0, alors elles ne retourne que les bons matches(suffisant pour le reste du programme)
        return len(good_matches)                                        
    
    elif choix == 1:                                                    #Si notre choix = 1, alors le programme trace les matches et permet un rendu visuel, une option que peut choisir l'user
        knn_matches = []
        for i in good_matches:
            paire = [i]                                                 #Récupération de chaque paire et ajout dans la liste knn_matches
            knn_matches.append(paire)
    
        
 
        result = cv2.drawMatches(cv2.cvtColor(logo, cv2.COLOR_BGR2RGB), keypoints_logo, cv2.cvtColor(image, cv2.COLOR_BGR2RGB), keypoints_image, good_matches, None,matchColor=(0, 255, 0), singlePointColor=(255, 0, 0), flags=2)
        
        plt.imshow(result)                                              #Dessin des matches entre les points sur les images pour le rendu visuel
        plt.show()                                                      #Affichage de la comparaison des deux images
        



def testing(img):                                                       #Fonction permettant de réaliser la comparaison entre l'images donées et les logos enregistré(imagettes)
    logos = liste_fichiers('images/imagettes')                          #Création de la liste comprenant les noms des imagettes
    resultat = []                                                       
    for i in range(len(logos)):                                         #boucle qui parcours la liste des logos
        x = comparaison(img, "images/imagettes/"+logos[i],0)            #Comparaison de logo avec l'image
        resultat.append({logos[i]:x})                                   #ajout dans les resultat du duo nom et performance en dictionaire clé valeur
        #print(f" le matching avec {logos[i]} est de {x}")
    return resultat                                                     #la fonction renvoie dans une liste touts les noms de logos avec leur performance 
    
def tri_meilleurs(dic):                                                 #Cette fonction renvoie un tri du des resultats de la fonction précédentes, affichant le logo avec la meilleure
                                                                        #correspondace ainsi que ceux se raprochant de la performance du meilleur
    src_max = ''                                                        
    max = 0
    for resultat in dic:
        x = next(iter(resultat.values()))                               #Simple algorithme permettant de trouver le max parmi les valeures (récupération de la value des dictionnaires)
        if x > max:
            max = x
            src_max = next(iter(resultat.keys()))
    
    print(f"Avec {max} correspondances, il est fort probable que le logo du club/pays : {src_max[:-4]} soit celui que vous recherchez") 
    
    for i in dic:                                                       #Touts logos qui aura une performance supérieur d'au minimum 50% de la meilleures performances sera considérer 
        if max * 0.5 < next(iter(i.values())) < max:                    #comme possibilité (pour contrer le manque de fiabilité de la méthode ORB)
            print(f" Il est également possible que le logo que vous cherchiez soit celui du club/pays : {next(iter(i.keys()))} ") 
            
    
      
    
    
      