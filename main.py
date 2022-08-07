import pypokedex
import PIL.Image , PIL.ImageTk
import tkinter as tk
from tkinter import *
from tkinter import ttk
import urllib3
from io import BytesIO
from PIL import ImageTk, Image

# cores ------------------------------------
co5 = "#ef5350"  # vermelha

# crio a janela
window = Tk()
window.geometry("400x620")
window.title("Pokedex")
window.config(padx=10, pady=10, bg=co5)
style = ttk.Style(window)
style.theme_use("clam")

title_label = tk.Label(window, text="Pokedex")
title_label.config(font=("Comfortaa", 32), bg=co5)
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

p_name = tk.Label(window, text="ID e Nome do pokemon:")
p_name.config(font=("Comfortaa", 17), bg=co5)
p_name.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 15), bg=co5)
pokemon_information.pack(padx=10, pady=10)

p_name = tk.Label(window, text="Tipo do pokemon:")
p_name.config(font=("Arial", 17), bg=co5)
p_name.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 15), bg=co5)
pokemon_types.pack(padx=10, pady=10)


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())


label_id_name = tk.Label(window, text="Inserir ID ou Nome")
label_id_name.config(font=("Arial", 20), bg=co5)
label_id_name.pack(padx=10, pady=5)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20), width=20)
text_id_name.pack(padx=10, pady=15)

btn_load = tk.Button(window, text="Buscar Pokemon", command=load_pokemon)
btn_load.config(font=("Arial", 20), height=2, width=13)
btn_load.pack(padx=10, pady=10)

window.mainloop()
