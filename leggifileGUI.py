import string
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def grafico():
    f = open(nome_file.get(), 'r')

    coordX = []
    coordY = []

    # da notare che posso fare un ciclo all'interno di un file
    # direttamente sulle righe

    for riga in f:
        valori = str(riga)  # converto in stringa la riga
        Nval = len(valori)          # conto il numero di caratteri
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y

    f.close()  # chiudiamo il file

    print ("X: ",coordX)
    print ("Y: ",coordY)

    # ordiniamo le liste
    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

    # stampo il tipo di dati delle coordinate
    print(type(coordX))
    print(type(coordY))

    # ora sono pronte per essere usate anche nei grafici

    plt.scatter(coordX,coordY)
    plt.ylabel('some numbers')
    plt.show()
    
root = tk.Tk()
root.geometry("250x55")
root.title("Leggi File")

nome_file = tk.Entry(root, text="Inserisci nome file", font = ("Tahoma",  12 ))
nome_file.grid()
nome_file.config(width=27)

bottone = tk.Button(root,command =grafico,  text="Genera il grafico", font = ("Tahoma",  12 ))
bottone.grid()
bottone.config(width=27)

root.mainloop()