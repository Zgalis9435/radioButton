import tkinter

window=tkinter.Tk() #Crear donde se ejecutaran los widgets

window.columnconfigure(1,weight=1)#Cantidad de columnas que dispone el formato grid y tamaño de las mismas
window.rowconfigure(2,weight=1)#Cantidad de filas que hay en la grid

seleccionado=tkinter.StringVar() #ASIGNA LA VARIABLE AL BOTON
seleccionado.set(None) #MANTIENE LAS OPCIONES SIN SELECCIONAR

def reset(event):# SI NO SE COLOCA EVENT NO FUNCIONA, ESTO SIRVE PARA DESELECCIONAR LOS BOTONES
    seleccionado.set(None)

rb1=tkinter.Radiobutton(window, text='Sin ánimo de lucro, de Algeciras',value='1',variable=seleccionado)
rb2=tkinter.Radiobutton(window, text='Alsoir con cafeina o sin cafeina',value='2',variable=seleccionado)
rb3=tkinter.Radiobutton(window, text='Hombre, sin ánimo de lucro, sin ánimo de lucro, una pizza o una tortilla de patatas'
                                     '¿tu que prefieres?',value='3',variable=seleccionado)
cleanButton=tkinter.Button(window, text='Haz click para quitar las opciones')

#CREACION DE LOS RADIOBUTTON

rb1.grid(column=0, row=0)
rb2.grid(column=0, row=1)
rb3.grid(column=0,row=2)
cleanButton.grid(column=1,row=0)

#CREACION DEL BOTON DE LIMPIEZA

cleanButton.bind('<Button-1>',reset)


window.mainloop() #Mantiene la ventana en ejecución




