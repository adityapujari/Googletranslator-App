from tkinter import *
import tkinter as tk
from googletrans import Translator
win=tk.Tk()
win.title("Translator")
win. geometry("200x200")
tkvar = StringVar(win)
choices = ['Hindi','French','Russian','Spanish','Japanese']
tkvar.set('Choose a language') # set the default option

popupMenu = OptionMenu(win, tkvar, *choices)
Label(win, text="").grid(row = 4, column = 0)
popupMenu.grid(row = 2, column =0)
# function for translator
def translation():
    word=entry.get()
    if tkvar.get()=='Hindi':
        translator=Translator(service_urls=['translate.google.com'])
        translation1= translator.translate(word,dest="hi")
        label1=tk.Label(win, text=f"translated in hindi:{translation1.text}",bg="yellow")
        label1.grid(row=4,column=0)
    elif tkvar.get()=='French':
        translator=Translator(service_urls=['translate.google.com'])
        translation1= translator.translate(word,dest="fr")
        label1=tk.Label(win, text=f"translated in French:{translation1.text}",bg="yellow")
        label1.grid(row=4,column=0)
    elif tkvar.get()=='Russian':
        translator=Translator(service_urls=['translate.google.com'])
        translation1= translator.translate(word,dest="ru")
        label1=tk.Label(win, text=f"translated in Russian:{translation1.text}",bg="yellow")
        label1.grid(row=4,column=0)
    elif tkvar.get()=='Spanish':
        translator=Translator(service_urls=['translate.google.com'])
        translation1= translator.translate(word,dest="es")
        label1=tk.Label(win, text=f"translated in Spanish:{translation1.text}",bg="yellow")
        label1.grid(row=4,column=0)
    elif tkvar.get()=='Japanese':
        translator=Translator(service_urls=['translate.google.com'])
        translation1= translator.translate(word,dest="ja")
        label1=tk.Label(win, text=f"translated in Japanese:{translation1.text}",bg="yellow")
        label1.grid(row=4,column=0)
label=tk.Label(win,text="Enter word:")
label.grid(row=0,column=0, sticky="W")
entry=tk.Entry(win)
entry.grid(row=1,column=0)
button=tk.Button(win,text="translate",command=translation)
button.grid(row=1,column=2)
win.mainloop()
