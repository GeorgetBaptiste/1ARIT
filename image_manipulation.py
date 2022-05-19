from tkinter.filedialog import *
import PIL.Image
from random import randint
from tkinter import *

class ImageManipulation:
    
    def __init__(self, screen_width, screen_height):
        
        font = ("Helvetica", 20, "bold")
        
        self.__root = Tk(className="Manipulation d'image")
        self.__root.geometry(str(screen_width)+"x"+str(screen_height))
        
        self.__canvas = Canvas(self.__root, width=screen_width, height=screen_height, highlightthickness=0, bg="black").place(x=screen_width*0.5, y=screen_height*0.5, anchor="center")
        self.__button_chiffrement_image_page = Button(self.__root, command=lambda:self.page(self.__page_chiffrement_image), text="Chiffrement image", width=20, pady=5, padx=10, font=font, fg="black", bg="white", highlightthickness=0, highlightbackground="black")
        self.__button_masquage_image_page = Button(self.__root, command=lambda:self.page(self.__page_masquage_image), text="Masquage image", width=20, pady=5, padx=10, font=font, fg="black", bg="white", highlightthickness=0, highlightbackground="black")
        self.__button_masquage_texte_page = Button(self.__root, command=lambda:self.page(self.__page_masquage_texte), text="Masquage texte", width=20, pady=5, padx=10, font=font, fg="black", bg="white", highlightthickness=0, highlightbackground="black")
        self.__button_back = Button(self.__root, command=lambda:self.page(self.__page_back), text="Retour", width=6, pady=2, padx=2, font=font, fg="black", bg="white", highlightthickness=0, highlightbackground="black")
        self.__button_chiffrer = Button(self.__root, command=lambda:self.chiffrer_dechiffrer_image(self.open_file("Choix de l'image"), self.open_file("Choix de l'image clé"), self.save_file("Où sauvegarder l'image")), text="Chiffrer image", width=20, pady=5, padx=10, font=font, fg="black", bg="white", highlightthickness=0, highlightbackground="black")
        self.__button_dechiffrer = Button(self.__root, command=lambda:self.chiffrer_dechiffrer_image(self.open_file("Choix de l'image"), self.open_file("Choix de l'image clé"), self.save_file("Où sauvegarder l'image")), text="Dechiffrer image", width=20, pady=5, padx=10, font=font, fg="black", bg="white", highlightthickness=0, highlightbackground="black")
        self.__entry = Entry(self.__root, width=24, font=font, fg="black", bg="white", highlightthickness=0, highlightbackground="black")
        self.__button_masquer_image = Button(self.__root, command=lambda: self.masquer_demasquer_image(self.open_file("Choix de l'image"), self.open_file("Choix de l'image clé"), int(self.get_entry()), "masquer", self.save_file("Où sauvegarder l'image")), text="Masquer image", width=20, pady=5, padx=10, font=font, fg="black", bg="white", highlightthickness=0, highlightbackground="black")
        self.__button_demasquer_image = Button(self.__root, command=lambda: self.masquer_demasquer_image(self.open_file("Choix de l'image"), self.open_file("Choix de l'image clé"), int(self.get_entry()), "demasquer", self.save_file("Où sauvegarder l'image")), text="Demasquer image", width=20, pady=5, padx=10, font=font, fg="black", bg="white", highlightthickness=0, highlightbackground="black")
        self.__button_masquer_texte = Button(self.__root, command=lambda: self.masquer_texte(self.open_file("Choix de l'image"), self.get_entry(), self.save_file("Où sauvegarder l'image")), text="Masquer texte", width=20, pady=5, padx=10, font=font, fg="black", bg="white", highlightthickness=0, highlightbackground="black")
        self.__button_demasquer_texte = Button(self.__root, command=lambda: self.demasquer_texte(self.open_file("Choix de l'image")), text="Demasquer texte", width=20, pady=5, padx=10, font=font, fg="black", bg="white", highlightthickness=0, highlightbackground="black")

        self.__button_chiffrement_image_page_p = (screen_width*0.5, screen_height*0.25)
        self.__button_masquage_image_page_p = (screen_width*0.5, screen_height*0.5)
        self.__button_masquage_texte_page_p = (screen_width*0.5, screen_height*0.75)
        self.__button_back_p = (screen_width*0.2, screen_height*0.1)
        self.__button_chiffrer_p = (screen_width*0.5, screen_height*0.4)
        self.__button_dechiffrer_p = (screen_width*0.5, screen_height*0.6)
        self.__entry_p = (screen_width*0.5, screen_height*0.4)
        self.__button_masquer_image_p = (screen_width*0.5, screen_height*0.6)
        self.__button_demasquer_image_p = (screen_width*0.5, screen_height*0.8)
        self.__button_masquer_texte_p = (screen_width*0.5, screen_height*0.6)
        self.__button_demasquer_texte_p = (screen_width*0.5, screen_height*0.8)
                
        self.__page_masquage_texte = [[self.__button_back, self.__entry, self.__button_masquer_texte, self.__button_demasquer_texte], [self.__button_back_p, self.__entry_p, self.__button_masquer_texte_p, self.__button_demasquer_texte_p]]
        self.__page_masquage_image = [[self.__button_back, self.__entry, self.__button_masquer_image, self.__button_demasquer_image], [self.__button_back_p, self.__entry_p, self.__button_masquer_image_p, self.__button_demasquer_image_p]]
        self.__page_chiffrement_image = [[self.__button_back, self.__button_chiffrer, self.__button_dechiffrer], [self.__button_back_p, self.__button_chiffrer_p, self.__button_dechiffrer_p]]
        self.__page_accueil = [(self.__button_chiffrement_image_page, self.__button_masquage_image_page, self.__button_masquage_texte_page), (self.__button_chiffrement_image_page_p, self.__button_masquage_image_page_p, self.__button_masquage_texte_page_p)]
        
        self.__page_back = None
        self.__page_actuel = self.__page_accueil
        self.page(self.__page_actuel)
        
        self.__root.mainloop()
    
    def page(self, page):
        self.__page_back = self.__page_actuel
        for i in range(len(self.__page_actuel[0])):
            self.__page_actuel[0][i].place_forget()
        for i in range(len(page[0])):
            page[0][i].place(x=page[1][i][0], y=page[1][i][1], anchor="center")
        self.__page_actuel = page
        self.__root.update()
    
    def chiffrer_dechiffrer_image(self, image=(), key_image=str(), name_save=str()):
        image_open = PIL.Image.open(image)
        key_image_open = PIL.Image.open(key_image)
        width_image = image_open.width
        height_image = image_open.height
        width_key_image = key_image_open.width
        height_key_image = key_image_open.height
        if width_image == width_key_image and height_image == height_key_image:
            new_image = PIL.Image.new(mode="RGB", size=(width_image, height_image))
            new_image_load = new_image.load()
            pixel_count = 0
            for x in range(width_image):
                for y in range(height_image):
                    r1, g1, b1 = image_open.getpixel((x, y))
                    r2, g2, b2 = key_image_open.getpixel((x, y))
                    r3, g3, b3 = r1^r2, g1^g2, b1^b2
                    new_image_load[x, y] = (r3, g3, b3)
                    pixel_count += 1
                    print("Chargement: ("+str(pixel_count)+"/"+str(width_image*height_image)+")")
            new_image.save(name_save)
                
    def create_key_image(self, width=int(), height=int(), name_save=str()):
        width, height = abs(width), abs(height)
        new_image = PIL.Image.new(mode="RGB", size=(width, height))
        new_image_load = new_image.load()
        pixel_count = 0
        for x in range(width):
            for y in range(height):
                new_image_load[x, y] = (randint(0, 255), randint(0, 255), randint(0, 255))
                pixel_count += 1
                print("Chargement: ("+str(pixel_count)+"/"+str(width*height)+")")
        new_image.save(name_save)
    
    def masquer_demasquer_image(self, image=str(), key_image=str(), key=int(), action=str(), name_save=str()):
        key = abs(key)
        image_open = PIL.Image.open(image)
        key_image_open = PIL.Image.open(key_image)
        width_image = image_open.width
        height_image = image_open.height
        width_key_image = key_image_open.width
        height_key_image = key_image_open.height
        if width_image == width_key_image and height_image == height_key_image:
            new_image = PIL.Image.new(mode="RGB", size=(width_image, height_image))
            new_image_load = new_image.load()
            pixel_count = 0
            for x in range(width_image):
                for y in range(height_image):
                    r1, g1, b1 = image_open.getpixel((x, y))
                    r2, g2, b2 = key_image_open.getpixel((x, y))
                    r3, g3, b3 = self.algo(action, r1, r2, key), self.algo(action, g1, g2, key), self.algo(action, b1, b2, key)
                    new_image_load[x, y] = (r3, g3, b3)
                    pixel_count+=1
                    print("Chargement: ("+str(pixel_count)+"/"+str(width_image*height_image)+")")
            new_image.save(name_save)
    
    def algo(self, action=str(), val1=int(), val2=int(), key=int()):
        if action == "masquer":
            val3 = round(val2+1/key*val1)
            if val3 > 255:
                val3 = 255
        elif action == "demasquer":
            val3 = key*(val1-val2)
        return val3
    
    def masquer_texte(self, image=str(), texte=str(), name_save=str()):
        chain_bin = ""
        i = 0
        image_open = PIL.Image.open(image)
        image_load = image_open.load()
        height = image_open.height
        width = image_open.width
        for caractere in range(len(texte)):
            chain_bin += self.str_to_bin(texte[caractere])
        if len(chain_bin) < (width*height*3):
            for y in range(height):
                if i < len(chain_bin):
                    for x in range(width):
                        if i < len(chain_bin):
                            rgb = list(image_open.getpixel((x, y)))
                            if rgb[0] == 255:
                                rgb[0] = 254
                            if rgb[1] == 255:
                                rgb[1] = 254
                            if rgb[2] == 255:
                                rgb[2] = 254
                            for z in range(len(rgb)):
                                if i < len(chain_bin):
                                    rgb[z] += int(self.str_to_bin(chr(rgb[z]))[-1])^int(chain_bin[i])
                                print("Chargement: ("+str(i)+"/"+str(len(chain_bin))+")")
                                i += 1
                            image_load[x, y] = tuple(rgb)
            image_open.save(name_save)
                
    def str_to_bin(self, string=str()):
        nb = ord(string)
        chain_bin = str(bin(nb))
        chain_bin = chain_bin[2:]
        while len(chain_bin) != 8:
            chain_bin = "0"+chain_bin
        return chain_bin
        
    def demasquer_texte(self, image=str()):
        image_open = PIL.Image.open(image)
        width = image_open.width
        height = image_open.height
        chain_bin = ""
        for y in range(height):
            for x in range(width):
                r, g, b = image_open.getpixel((x, y))
                rgb = [r, g, b]
                for z in range(len(rgb)):
                    if rgb[z]%2 == 1:
                        chain_bin += "1"
                    else:
                        chain_bin += "0"
                    print("Chargement: ("+str(len(chain_bin))+"/"+str(height*width*3)+")")
        print(self.bin_to_str(chain_bin))
                        
    def bin_to_str(self, chain_bin=str()):
        x, y = 0, 8
        texte = ""
        while y <= len(chain_bin) and len(texte) < 100:
            byte = chain_bin[x:y]
            mult = 1
            nb = 0
            for i in range(7, -1, -1):
                if byte[i] == "1":
                    nb = nb+(1*mult)
                mult *= 2
            texte += chr(nb)
            x += 8
            y += 8
        return texte
    
    def open_file(self, name):
        return askopenfilename(defaultextension=".bmp", filetypes=[("Fichier Bitmap", '*.bmp')], title=name)
    
    def save_file(self, name):
        return asksaveasfilename(defaultextension='.bmp', filetypes=[("Fichier Bitmap", '*.bmp')],title=name)
    
    def get_entry(self):
        return self.__entry.get()
        
test = ImageManipulation(400, 400)