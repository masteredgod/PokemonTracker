import customtkinter
from storage import load_pokemon
import requests
from PIL import Image
from io import BytesIO
import os


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.scroll_frame = customtkinter.CTkScrollableFrame(self)
        self.scroll_frame.pack(fill="both", expand=True)
        self.pokedex = load_pokemon()
        self.geometry("1080x720")
        self.title("Living Dex")

        self.load_button = customtkinter.CTkButton(self, text= "load more", command = self.load_more)
        self.load_button.pack()
        #self.button = customtkinter.CTkButton(self, text="pikachu", command=self.button_callback)
        #self.button.pack(padx=20, pady=20)
        self.loaded_Pokemon= 48
        i = 0
        for dex_number, pokemon in list(self.pokedex.items())[:self.loaded_Pokemon]:
            print(f"Processing {pokemon['Name']}")
            card = customtkinter.CTkFrame(self.scroll_frame)
            card.grid(row=i//6, column=i%6, padx=10, pady=10)
            if os.path.exists(f"pokemon_sprites/{pokemon["Dex_number"]}.png"):
                image = Image.open(f"pokemon_sprites/{pokemon["Dex_number"]}.png").convert("RGBA")
                ctk_image = customtkinter.CTkImage(image, size=(100,100))
                Image_label =customtkinter.CTkLabel(card, image=ctk_image, text="")
                Image_label.grid(row=0, column=0, padx=90, pady=50)

            
            
            card.text = customtkinter.CTkLabel(card, text=(pokemon["Name"]))
            card.text.grid(row=1, column=0, padx=90, pady=50)
            i += 1
        print("Loop finished")    
    
    def button_callback(self):
        print("button clicked")

    
    def load_more(self):
        old_amount = self.loaded_Pokemon
        self.loaded_Pokemon += 48   
        i = old_amount
        for dex_number, pokemon in list(self.pokedex.items())[old_amount:self.loaded_Pokemon]:
            card = customtkinter.CTkFrame(self.scroll_frame)
            card.grid(row=i//6, column=i%6, padx=10, pady=10)           
            if os.path.exists(f"pokemon_sprites/{pokemon["Dex_number"]}.png"):
                image = Image.open(f"pokemon_sprites/{pokemon["Dex_number"]}.png").convert("RGBA")
                ctk_image = customtkinter.CTkImage(image, size=(100,100))
                Image_label =customtkinter.CTkLabel(card, image=ctk_image, text="")
                Image_label.grid(row=0, column=0, padx=90, pady=50)

            
            
            card.text = customtkinter.CTkLabel(card, text=(pokemon["Name"]))
            card.text.grid(row=1, column=0, padx=90, pady=50)
            i +=1


app = App()
app.mainloop()