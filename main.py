import cv2
from customtkinter import *
from tkinter import *
from CTkListbox import *
import fonctions as fn
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


window = CTk()
window.title("WATIMIS")
window.iconbitmap("icon.ico")
screen_width, screen_height = window.winfo_screenwidth() - 200, window.winfo_screenheight() - 200

notice_utilisation = "WATIMIS est une application permettant d'identifié un club de ligue 1. \n Pour utiliser notre service, rien de plus simple, il vous suffit de prendre une photo du logo (provenant d'un maillot, d'une casquette...). \n Attention, pour le bon fonctionnement du logicel, veuillez prendre une photo la plus près possible du logo en question. \n Maintenant, il vous suffit juste de séléctionner cette image en cliquant juste en bas!"

window.geometry(f"{screen_width}x{screen_height}+0+0")

frame = CTkFrame(window, fg_color='transparent')
titre = CTkLabel(frame, text="Bienvenue sur WATIMIS", font=("Arial Black", 50))
titre.pack()
soustitre = CTkLabel(frame, text="Le logiciel de reconaissance de vos équipes préférées (édition Ligue1)", font=("Arial", 35))
soustitre.pack(pady=10)

notice = CTkLabel(frame, text=notice_utilisation, font=("Arial", 25))
notice.pack(pady=10)

def verification():
    fn.check(window)
    

Selection = CTkButton(master=window, text='Sélectionner un fichier', command=fn.select_file)
destruction = CTkButton(master=window, text='Continuer', command=verification)

frame.pack(pady=screen_height * 0.3)
Selection.pack(pady=10)
destruction.pack(pady=0)

window.mainloop()

##########################################################################################################################################

x, y = fn.tri_meilleurs(fn.testing())

poss1 = next(iter(y[1].keys()))
poss2 = next(iter(y[2].keys()))
poss3 = next(iter(y[3].keys()))

print(poss1)

# fig =plt.imshow(fn.comparaison('images/'+x,img,1))  

fig, ax = plt.subplots(figsize=(screen_width / 100+2, screen_height / 100 +1  ))
ax.imshow(fn.comparaison('images/' + x, fn.path_retour(), 1))
ax.axis("off")  
plt.close(fig)  
##########################################################################################################################################

page = CTk()
page.title("WATIMIS")
page.iconbitmap("icon.ico")
page.geometry(f"{screen_width}x{screen_height}")
page.configure(fg_color="black")

frame1 = CTkFrame(master=page, fg_color='black', width=screen_width * 0.66, height=screen_height, corner_radius=0)
frame2 = CTkFrame(master=page, fg_color='black', width=screen_width * 0.33, height=screen_height, corner_radius=0)

frame1.grid_propagate(False)
frame2.grid_propagate(False)

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=1, sticky="nsew")

Resultat_titre = CTkLabel(master=frame1, text=f"Selon nos calcul, il est fort probable que le club \n que vous cherchiez soit {x[:-4]} !",font=CTkFont(size=30))
Resultat_titre.pack(pady = 10)

canvas = CTkCanvas(frame1, width=screen_width*1.33, height=800)
canvas.pack(expand=True)

canvas2 = FigureCanvasTkAgg(fig, master=canvas)
canvas_widget = canvas2.get_tk_widget()
canvas_widget.pack()

Possibilite_titre = CTkLabel(master=frame2, text="Mais il est possible que votre logo \n soit celui de :", font=CTkFont(size=20))
Possibilite_titre.pack(pady = 10, padx = 10)

#######################################################


Possibilite_1 = CTkFrame(master=frame2, fg_color='transparent', width=screen_width * 0.33, height=screen_height * 0.3, corner_radius=0)
Possibilite_1_nom = CTkLabel(master=Possibilite_1, text=poss1[:-4])

Possibilite_1.pack()
Possibilite_1_nom.pack()

img = "images/" + poss1

try:
    image = Image.open(img).resize((200, 200))  
    photo = ImageTk.PhotoImage(image)
except FileNotFoundError:
    print(f"Erreur : le fichier '{img}' est introuvable.")
    photo = None 

canvas = Canvas(Possibilite_1, width=250, height=200, background="Black",highlightbackground="black")
if photo: 
    canvas.create_image(0, 0, anchor="nw", image=photo)
    Possibilite_1.photo = photo  
canvas.pack()

#######################################################

Possibilite_2 = CTkFrame(master=frame2, fg_color='transparent', width=screen_width * 0.33, height=screen_height * 0.3, corner_radius=0)

Possibilite_2_nom = CTkLabel(master=Possibilite_2, text=poss2[:-4])

Possibilite_2.pack()
Possibilite_2_nom.pack()

img = "images/" + poss2

try:
    image = Image.open(img).resize((200, 200))  
    photo = ImageTk.PhotoImage(image)
except FileNotFoundError:
    print(f"Erreur : le fichier '{img}' est introuvable.")
    photo = None  

canvas = Canvas(Possibilite_2, width=250, height=200,background="Black",highlightbackground="black")
if photo: 
    canvas.create_image(0, 0, anchor="nw", image=photo)
    Possibilite_2.photo = photo 
canvas.pack()

#####################################################

Possibilite_3 = CTkFrame(master=frame2, fg_color='transparent', width=screen_width * 0.33, height=screen_height * 0.3, corner_radius=0)


Possibilite_3_nom = CTkLabel(master=Possibilite_3, text=poss3[:-4])

Possibilite_3.pack()
Possibilite_3_nom.pack()

img = "images/" + poss3

try:
    image = Image.open(img).resize((200, 200))  
    photo = ImageTk.PhotoImage(image)
except FileNotFoundError:
    print(f"Erreur : le fichier '{img}' est introuvable.")
    photo = None  

canvas = Canvas(Possibilite_3, width=250, height=200, background="Black",highlightbackground="black")
if photo:  
    canvas.create_image(0, 0, anchor="nw", image=photo)
    Possibilite_3.photo = photo 
canvas.pack()

page.mainloop()
