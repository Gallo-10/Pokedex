# Pokedex
A simple Pokedex made with python.


## 🔧 How it was made
The app was made using the pypokedex library to get the pokemon's database, Tkinker to build its interface, urllib3 to get the sprites from pypokedex and Pillow with BytesIO to manage these sprites of the pokemon. 


## ⚙️How it works
Basically everythig works around a simple function that gathers all the info about the pokemon the user is searching and converts the sprite given by pypokedex into a image to show on the app.

```
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
```


## 📋 How to use
To use the app insert the ID number or the name of the Pokemon and press the button to search it. 
