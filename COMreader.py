import tkinter as tk
import serial.tools.list_ports
import serial
import time

window = tk.Tk()
window.title("COM Port reader")
window.geometry("600x400")
window.resizable(True, True)
window.config(bg="#232323")

ser = serial.Serial('COM5', 9600)

def leggicom():
    leggi = serial.Serial('COM5', 9600) #You can modify this

    while True:
        valore = leggi.readline()
        valoreinstringa = str(valore, "UTF-8")
        print(valoreinstringa)
        window.update

def com():
    porte_disponibili = list(serial.tools.list_ports.comports()) #Prende la lista delle porte COM attive
    if porte_disponibili: #Se c'è una porta disponibile...
        nome_porta = porte_disponibili[0].device #Ne prende il nome con il [0] che sarebbe il primo elemento della lista delle porte COM trovate aperte
        labelcom.config(text=f"Porta COM in uso trovata: {nome_porta}") #Configura la Label che andarà a far vedere il risultato
    else:  #Se non trova porte COM attive...
        labelcom.config(text="Nessuna porta COM in uso.") #Configura la Label che andarà a far vedere il risultato

def manda():
    global ser
    testoricevuto = testo.get("1.0", tk.END).rstrip()
    if ser and ser.is_open:
        if testoricevuto:
            try:
                testo_bytes = testoricevuto.encode('utf-8')
                ser.write(testo_bytes)
                print(f"Inviato: {testoricevuto}")
                testo.delete("1.0", tk.END)
            except serial.SerialException as e:
                print(f"Errore nell'invio: {e}")
        else:
            print("Nessun testo da inviare.")
    else:
        print("Porta seriale non aperta per l'invio.")

tasto = tk.Button(window, text="Check COM", command=com, width=18, height=5, bg="#cadbce", fg="black")
tasto.grid(row=1, column=0, padx=20, pady=15)

labelcom = tk.Label(window, text="Check COM ports...")
labelcom.grid(row=1, column=2, padx=0, pady=15)

tastoread = tk.Button(window, text="Read data", command=leggicom, width=18, height=5, bg="#cadbce", fg="black")
tastoread.grid(row=1, column=1, padx=40, pady=30)

testo = tk.Text(window, height=5, width=30) # Crea la textbox con altezza di 5 righe e larghezza di 30 caratteri
testo.grid(row=0, column=0, padx=10, pady=10)

tastotesto = tk.Button(window, text="Send code", command=manda, width=18, height=5, bg="#cadbce", fg="black")
tastotesto.grid(row=3, column=1, padx=10, pady=15)

window.mainloop()