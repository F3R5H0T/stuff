from tkinter import *    
from tkinter import ttk 
import preguntas as p
import time
def grafica():
	root=Tk()
	root.geometry('500x300')
	root.configure(bg = 'blue')
	root.title("Brain Train")
	texto=StringVar()
	la=Label(root, textvariable=texto, relief=RAISED, bg='white', foreground="black").pack(side=TOP)
	ttk.Button(root, text='Salir', command=quit).pack(side=BOTTOM)
	texto.set("Villano: {}\nVidas:{}".format(p.villano,p.vidas))
	gengar=Canvas(root, width=100,height=100, bg="blue")
	gengar.pack(side=RIGHT)
	player=Canvas(root, width=100,height=100, bg="blue")
	player.pack(side=LEFT)
	imgg = PhotoImage(file="C:\\Users\\ferch\\Pictures\\Tareas\\Gengar.gif")
	gengar.create_image(20,20, anchor=NW, image=imgg)
	imgp = PhotoImage(file="C:\\Users\\ferch\\Pictures\\Tareas\\leaf.gif")
	player.create_image(20,20, anchor=NW, image=imgp)
	p.play()
	#if p.villano==0:
	#	imgg= PhotoImage(file="C:\\Users\\ferch\\Pictures\\Tareas\\tauros.gif")
	#	gengar.create_image(20,20, anchor=NW, image=imgg)
	root.mainloop()
def update():
	la.after(500, update)
grafica()
update()