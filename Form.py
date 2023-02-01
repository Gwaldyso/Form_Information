# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:22:26 2023

@author: Administrator
"""
from tkinter import *
from tkinter import messagebox

"""fenetrePrincipale = Tk()
l = Label(fenetrePrincipale, text = "Nom")
l.pack()

fenetrePrincipale.mainloop()"""

fenetrePrincipale = Tk()
l = Label(fenetrePrincipale, text = "Nom & prénom").grid(row = 0, column = 0)
l1 = Label(fenetrePrincipale, text = "Sexe").grid(row = 2, column = 0)
l2 = Label(fenetrePrincipale, text = "Age").grid(row = 1, column = 0)
l3 = Label(fenetrePrincipale, text = "Continent").grid(row = 3, column = 0)
l3 = Label(fenetrePrincipale, text = "Centre d'interet").grid(row = 4, column = 0)



e = Entry(fenetrePrincipale).grid(row = 0, column = 1)
e1=Entry(fenetrePrincipale).grid(row = 1, column = 1)




rb1 = Radiobutton(fenetrePrincipale, text = "Feminin", value = '1').grid(row = 2, column = 1)
rb2 = Radiobutton(fenetrePrincipale, text = "Masculin", value = '2').grid(row = 2, column = 2)

#l2=Label(fenetrePrincipale, text = "Hobbies")
c1 = Checkbutton (fenetrePrincipale, text = "art", variable = '1').grid(row = 4, column = 1)
c2 = Checkbutton (fenetrePrincipale, text = "science", variable = '2').grid(row = 4, column = 2)
c3 = Checkbutton (fenetrePrincipale, text = "litterature", variable = '3').grid(row = 4, column = 3)
c4 = Checkbutton (fenetrePrincipale, text = "Autres", variable = '4').grid(row = 4, column = 4)



lb = Listbox(fenetrePrincipale)
lb.insert(0, 'Asie')
lb.insert(1, 'Afrique')
lb.insert(2, 'Amérique')
lb.insert(3, 'Europe')
lb.grid(row = 3, column = 1)

def SendForm():
    messagebox.showinfo("Statut de l'inscription","Formulaire envoyé")

b = Button(fenetrePrincipale ,text="Submit") #créer un bouton

print("hello world")

fenetrePrincipale.mainloop()