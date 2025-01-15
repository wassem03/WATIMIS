#Fichier comprenant toutes les fonctions nécessaire au bon fonctionnement du programme

#######################################################################################

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
from tkinter import filedialog, messagebox
from tkinter import*
from PIL import Image, ImageTk  # Pour gérer les images

######################################################################################

path = ''

def select_file():
    """Ouvrir une boîte de dialogue pour sélectionner une image et l'afficher."""
    file_path = filedialog.askopenfilename(
        title="Sélectionnez une image",
        filetypes=(("Images PNG", "*.png"), ("Images JPG", "*.jpg"), ("Images JPEG", "*.jpeg"), ("Tous les fichiers", "*.*"))
    )
    if file_path:  
        print(file_path)
        global path 
        path = file_path
            

def check(fenetre):
    global path
    if not path:
        window = Tk()
        window.geometry("500x200")
        label = Label(window, text="Veuillez sélectionner un fichier")
        label.pack()
        window.mainloop()
    else: 
        fenetre.destroy()
        



def liste_fichiers(dossier):                                            #Création de la fonction permettant de donner une liste contenant le nom de tout les fichiers d'un dossier
    fichiers = []
    for fichier in os.listdir(dossier):
        if os.path.isfile(os.path.join(dossier, fichier)):              #Vérification si le dossier comporte un fichier
            fichiers.append(fichier)                                    #Ajout du nom du fichier dans une liste prévue a cet effet
                                                                        
    return fichiers                                                     #Revoie la liste contenant les fichiers présents dans le dossier
 
def redimensionner(image):    
    height, width = image.shape[:2]   
    ratio = 500/height
    width = width * ratio
    return cv2.resize(image,(500,int(500)),interpolation=cv2.INTER_AREA)
   

def comparaison(nom_image,nom_logo,choix):                              #Creation de la fonction principale qui effectue la comparaison des images entres elles grace à la methode ORB
                                                                        #Cette fonction prend en compte l'image, un logo, et un choix binaire qui sera expliquer ensuite    
    image = cv2.imread(nom_image, cv2.IMREAD_COLOR)
    logo = redimensionner(cv2.imread(nom_logo, cv2.IMREAD_COLOR))                       #Lecture des images
   
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
        return result
                                                            #Affichage de la comparaison des deux images
        


def tri_possible(liste_dicos):
    tuples = [(list(d.keys())[0], list(d.values())[0]) for d in liste_dicos]
    tuples_triees = sorted(tuples, key=lambda x: x[1], reverse=True)
    top_4 = tuples_triees[:4]
    return [{k: v} for k, v in top_4]






def testing(): 
    global path   
    img = path                                                  #Fonction permettant de réaliser la comparaison entre l'images donées et les logos enregistré(imagettes)
    logos = liste_fichiers('images')                          #Création de la liste comprenant les noms des imagettes
    resultat = []                                                       
    for i in range(len(logos)):                                         #boucle qui parcours la liste des logos
        
        x = comparaison(img, "images/"+logos[i],0)            #Comparaison de logo avec l'image
        resultat.append({logos[i]:x})                                   #ajout dans les resultat du duo nom et performance en dictionaire clé valeur
        #print(f" le matching avec {logos[i]} est de {x}")
    print(resultat)
    return resultat                                                     #la fonction renvoie dans une liste touts les noms de logos avec leur performance 
    
def tri_meilleurs(dic):                                                 #Cette fonction renvoie un tri du des resultats de la fonction précédentes, affichant le logo avec la meilleure
                                                                        #correspondace ainsi que ceux se raprochant de la performance du meilleur
    src_max = ''                                                        
    max = 0
    possibilite = []
    for resultat in dic:
        x = next(iter(resultat.values()))                               #Simple algorithme permettant de trouver le max parmi les valeures (récupération de la value des dictionnaires)
        if x > max:
            max = x
            src_max = next(iter(resultat.keys()))
    
    print(f"Avec {max} correspondances, il est fort probable que le logo du club/pays : {src_max[:-4]} soit celui que vous recherchez") 
    """
    for i in dic:                                                       #Touts logos qui aura une performance supérieur d'au minimum 50% de la meilleures performances sera considérer 
        if max * 0.5 < next(iter(i.values())) < max:                    #comme possibilité (pour contrer le manque de fiabilité de la méthode ORB)
            print(f" {next(iter(i.values()))} : {next(iter(i.keys()))} ") 
            possibilite.append(next(iter(i.keys())))"""
            
    top4 = tri_possible(dic)
    return src_max, top4
            
    
def path_retour():
    global path
    return path
    
    
      