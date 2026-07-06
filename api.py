import requests

def get_pokemon(name):
        try:
            response = requests.get( f"https://pokeapi.co/api/v2/pokemon/{name}")

            typing_list = []
            for types in response.json()["types"]:
                typing_list.append(types["type"]["name"])
            
        
            return {
                  "Dex_number": str(response.json()["id"]).zfill(3),
                  "Name": response.json()["name"],
                  "Typing": typing_list,
                  "Owned": False,
                  "Shiny": False,
                  "stored": "",
                  "sprite": response.json()["sprites"]["other"]["home"]["front_default"]
                  }
        except:
             return None
        