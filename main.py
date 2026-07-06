from is_shiny import OwnedYN 
from games import Games
from pokemon import Pokemon
from api import  get_pokemon
from storage import save_pokemon, load_pokemon,save_sprite

total_pokemon = 1025
pokedex = load_pokemon()


if pokedex =={}:
    for i in range(1,total_pokemon +1):
        Pokemon = get_pokemon(i)
        if Pokemon == None:
            print("Failed to connect to api, please try again")
            continue
        pokedex[Pokemon["Dex_number"]] = Pokemon
        print(f"Fetched {Pokemon['Name']} - {Pokemon["Dex_number"]}")
    save_pokemon(pokedex)
    print("About to save sprites")





## Pokemon-Search function
while True:
    found = False
    Owned_number = 0
    
    user_input = input("Search Pokemon: ")
    if user_input == "quit":
        break
    if user_input == "unowned":
        for dex_number, Pokemon in pokedex.items():
            if Pokemon["Owned"] == False:
                print ( f"{Pokemon["Name"].capitalize()} - #{Pokemon["Dex_number"]}")
        found = True
    if user_input == "owned":
        for dex_number, Pokemon in pokedex.items():
            if Pokemon["Owned"] == True:
                print ( f"{Pokemon["Name"].capitalize()} - #{Pokemon["Dex_number"]} - stored: {Pokemon["stored"]}")
        found = True
    if user_input == "owned/unowned":
        for dex_number, Pokemon in pokedex.items():
            if Pokemon["Owned"] == True:
                Owned_number += 1
        Unowned_number = total_pokemon - Owned_number
        print(f"you own {Owned_number} Pokemon, out of {total_pokemon}. {Owned_number/total_pokemon*100:.2f}%")
        print(f"your total number of unowned pokemon is {Unowned_number} ")
        found = True



    for dex_number, Pokemon  in pokedex.items():
        if user_input.lower() in Pokemon["Name"].lower():
            found = True
            print ( f"{Pokemon["Name"].capitalize()} - #{Pokemon["Dex_number"]}")
            if len(Pokemon["Typing"])!= 1:
                print (f"{Pokemon["Typing"][0]}, {Pokemon["Typing"][1]}")
            else:
                print (f"{Pokemon["Typing"][0]}")
            if Pokemon["Owned"] == True:
                print("Owned?: Yes")
            else:
                print("Owned?: No")

            if Pokemon["Shiny"] == True:
                print("Shiny?: Yes")
            else:
                print("Shiny?: No") 
        
            print (f"stored location: {Pokemon["stored"]}")

            print("...")

            print()
            Stored_update = input("Do you Want to update This Pokemon y/n?: ")
            if Stored_update.lower() == "y":
                if Pokemon["Owned"] == False:
                    for key, value in Games.items():
                        print (f"{key}: {value}")
                    Location_update = input(" what game?:")
                    Pokemon["stored"] = Games[Location_update]
                    Pokemon["Owned"] = True
                    Shiny_update = input("is it shiny y/n?:").lower()
                    Pokemon["Shiny"] = OwnedYN[Shiny_update]
                    save_pokemon(pokedex)
                elif Pokemon["Owned"] == True:
                    Ownership_removal = input("Do you want to unown your pokemon y/n?: ")
                    if Ownership_removal.lower() == "y":
                        Pokemon["Owned"] = False
                        Pokemon["Shiny"] = False
                        Pokemon["stored"] = ""
                        save_pokemon(pokedex)            

    if found == False:
        print(f"Pokemon not found: {user_input}?") 
        
    