import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext
ventana=tk.Tk()
ventana.title("Examen de Programación")
ventana.geometry("920x520")
ttk.Label(ventana, text="Primer examen de Programación").grid(column=1,row=0)
def clickMe():
    calificacion=0
    if(Pregunta1.get()=="if():"):calificacion=calificacion+2
    if(Pregunta2.get()=="tkinter"):calificacion=calificacion+2
    if(opcion.get()=="INT"):calificacion=calificacion+2
    if(opcion2.get()=="Pila"):calificacion=calificacion+2
    if(opcion_1.get()==1 and opcion_4.get()==1 and opcion_2.get()==0 and opcion_3.get()==0 and opcion_5.get()==0):calificacion=calificacion+2
    ventana2=tk.Tk()
    ventana2.title("Calificacion")
    ttk.Label(ventana2,text="La calificacion es: "+str(calificacion)).grid(column=0, row=0)

#Text Boxes
Pregunta1=tk.StringVar()
t1=ttk.Label(ventana, text="Escriba como se declara una condicion en python: ").grid(column=0, row=1)
Pregunta1Capturada = ttk.Entry(ventana, width=20, textvariable=Pregunta1).grid(column=1, row=1)
Pregunta2=tk.StringVar()
t2=ttk.Label(ventana, text="Diga que librería es necesaria para usar ventanas en python:").grid(column=0, row=2)
Pregunta2Capturada = ttk.Entry(ventana, width=20, textvariable=Pregunta2).grid(column=1,row=2)

#RadioButton
ttk.Label(ventana, text="Selecciona el tipo de una variable entera").grid(column=1, row=3)
opcion=tk.StringVar()
radio1=tk.Radiobutton(ventana, text="INT", variable=opcion,value="INT")
radio1.grid(column=0, row=4, sticky=tk.W)
radio2=tk.Radiobutton(ventana, text="FLOAT", variable=opcion,value="FLOAT")
radio2.grid(column=1, row=4, sticky=tk.W)
radio3=tk.Radiobutton(ventana, text="DOUBLE", variable=opcion,value="DOUBLE")
radio3.grid(column=2, row=4, sticky=tk.W)

ttk.Label(ventana, text="El primero en entrar es el último en salir\ny el último en entrar es el primero en salir").grid(column=1, row=5)
opcion2=tk.StringVar()
radio4=tk.Radiobutton(ventana, text="Pila", variable=opcion2,value="Pila")
radio4.grid(column=0, row=6, sticky=tk.W)
radio5=tk.Radiobutton(ventana, text="Cola", variable=opcion2,value="Cola")
radio5.grid(column=1, row=6, sticky=tk.W)
radio6=tk.Radiobutton(ventana, text="Lista", variable=opcion2,value="Lista")
radio6.grid(column=2, row=6, sticky=tk.W)

#Check Button
ttk.Label(ventana, text="Seleccione los tipos de variable númericas").grid(column=1, row=9)
opcion_1=tk.IntVar()
casilla_1=tk.Checkbutton(ventana, text="INT", variable=opcion_1)
casilla_1.deselect()
casilla_1.grid(column=0, row=10, sticky=tk.W)
opcion_2=tk.IntVar()
casilla_2=tk.Checkbutton(ventana, text="BOOLEAN", variable=opcion_2)
casilla_2.deselect()
casilla_2.grid(column=1, row=10, sticky=tk.W)
opcion_3=tk.IntVar()
casilla_3=tk.Checkbutton(ventana, text="String", variable=opcion_3)
casilla_3.deselect()
casilla_3.grid(column=2, row=10, sticky=tk.W)
opcion_4=tk.IntVar()
casilla_4=tk.Checkbutton(ventana, text="DOUBLE", variable=opcion_4)
casilla_4.deselect()
casilla_4.grid(column=0, row=11, sticky=tk.W)
opcion_5=tk.IntVar()
casilla_5=tk.Checkbutton(ventana, text="Char", variable=opcion_5)
casilla_5.deselect()
casilla_5.grid(column=1, row=11, sticky=tk.W)

#Button
accion2=ttk.Button(ventana, text="Calificar",command=clickMe)
accion2.place(x=810,y=270)

ventana.mainloop()