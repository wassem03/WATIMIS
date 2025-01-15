#Ce programme est le "main", il sera celui à executer afin de lancer le programme, il fait le liens entre toutes les fonctions crée avant
#Pour l'utiliser, il suffit d'entrer le chemin d'une images (exemple ci dessous) et de choisir si on souhaite obtenir au préalable un rendu visuel
#de chaque comparaison avant d'obtenir le verdict final

#exemple de cemin à donner:  images/images_a_traiter/ol2.png     images/images_a_traiter/algerie1.jpeg    

#######################################################################################

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import fonctions as fn

#######################################################################################
  
print("Bonjour, bienvenue sur Watimis, le service de reconaissance de vos équipes de football préférées")
img = input("Pour utiliser notre service, je vous laisse entrer le path de votre image:")   #Demande du chemin de l'image que l'user souhaite analyser
print("Souhaitez vous obtenir un rendu visuel? Y or N:")                                    #Demande d'un potentiel rendu visuel
choix = input("votre réponse:")
while True:
    if choix == 'N' or choix == 'n':                                                        #Dans le cas d'un refus, l'algorithme revoie directement les résultats
        print("Ok, c'est parti!")
        print(fn.tri_meilleurs(fn.testing(img)))                                            #On teste les performances de chaques logos avant de les trier et d'obtenir le/les meilleur(s) 
        break                                                                               #On sort de la boucle
    elif choix == 'Y' or choix == 'y':
        liste = fn.liste_fichiers("images/imagettes")
        for i in liste:
            fn.comparaison(img,"images/imagettes/"+i,1)                                     #dans le cas de d'une acceptation, on renvoie chaque comparaison visuelle(on notera le 1 en tant que dernier argument)
        
        print(fn.tri_meilleurs(fn.testing(img)))                                            #Encore une fois on renvoie le/les meilleur(s) résultat
        break
    else:                                                                                   #Dans le cas ou l'user se trompe, on redemande son choix en faisant bien attention 
        print("Attention, il ne faut répiondre que par Y ou N!")
        choix = input("votre réponse:")
    
print("merci d'avoir usée de nos services")
    
    