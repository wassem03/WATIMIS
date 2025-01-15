#Le fichier large test permet de lancer une comparaison massive sur toutes les images du jeu de données
#les résultats seront données dans le fichier txt "resultat_large_test.txt"
#Nous avions choisi ce format car il permet une bien meilleure lisibilitée
#il suffit ensuite de comparer le nom de l'image (ce qui explique leur nom si explicite) avec le résultat de la détection avoir de se rendre compte
#lorsque le programme à réussi à deviner ou s'est tromper (ou a trouver mais pas en sont premier choix)


#######################################################################################################

import cv2
import numpy as np
import os
import fonctions as fn

#######################################################################################################

liste_images = fn.liste_fichiers("images/images_a_traiter")             #création d'une liste comprenant toutes les images(à traiter, pas les logos)

with open("resultat_large_test.txt", 'w') as fichier:                   #Ouverture et réinitialisation du fichier txt comportant les résultat
    pass  

fichier = open("resultat_large_test.txt", "a")


def accord(img):                                                        #Création de la fonction accord qui renvera la/les meilleure(s) correspondance par rapport au logo
    logos = fn.liste_fichiers('images/imagettes')                       #Création d'une liste comprenant tout les logos
    dic = []
    for i in range(len(logos)):                                         #Boucle faisant la comparaison (voir fichier des fonctions) entre les logos et l'images données
        x = fn.comparaison(img, "images/imagettes/"+logos[i],0)
        if x is not None:
            dic.append({logos[i]:x})                                    #Ajout en format dictionnaire les logos et leur performances en tant que clé-valeur
        #print(f" le matching avec {logos[i]} est de {x}")
        
    src_max = ''
    max = 0
    
    for resultat in dic:
        x = next(iter(resultat.values()))                               #Récupération de la performance chaque imagettes
        if x > max:
            max = x                                                     #Comparaison entre celles ci pour ne garder que la meilleures
            src_max = next(iter(resultat.keys()))
    possibilite = []        
    for i in dic:
        if max * 0.5 < next(iter(i.values())) < max:                    #Touts logos qui aura une performance supérieur d'au minimum 50% de la meilleures performances entrera dans 
            possibilite.append(next(iter(i.keys())))                    # la liste des possibilitées (pour prévenir les éventuelles erreurs du logiciel)

    
    print(f"{img} correspond à {src_max[:-4]}, possibilités: {possibilite} ")  
    fichier.write(f"{img} correspond à {src_max[:-4]}, possibilités: {possibilite} ")
    fichier.write("\n")                                                 #ecriture du résultat dans le fichier txt



for i in liste_images:
    accord("images/images_a_traiter/"+i)                                #Boucle qui permet le traitement de toutes les images du dossier

fichier.close()