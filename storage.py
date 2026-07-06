import json
import os
import requests


def save_pokemon(pokedex):
    with open("pokemon_data.json", "w") as f:
        json.dump(pokedex, f, indent=4)

def load_pokemon():
    try:
        with open("pokemon_data.json", "r") as f:
            return json.load(f)
        
    except:
        return{}
    
def save_sprite(pokedex):
    print("save_sprite called")
    for Dex_number, pokemon in pokedex.items():
        print(f"looping: {Dex_number}")
        print(f"Downloading: {pokemon["Name"]}")
        if pokemon["sprite"] == "None" or pokemon["sprite"] is None:
            continue
        response = requests.get(pokemon["sprite"])
        with open(f"pokemon_sprites/{pokemon["Dex_number"]}.png", "wb")as f:
            f.write(response.content)

