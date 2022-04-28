from tkinter import *

class Interface:
    
    def __init__(self, screen_width, screen_height):
        
        self.__root = Tk(className="1ARIT")
        self.__root.geometry(str(screen_width)+"x"+str(screen_height))
        self.__root.attributes('-fullscreen', True)
        
        self.__canvas = Canvas(self.__root, width=screen_width, height=screen_height, highlightthickness=0, bg="red")
        self.__canvas.place(x=screen_width/2, y=screen_height/2, anchor="center")
        
        self.__button_chiffrement_image = Button(self.__root, text="Chiffrement image", width=20, pady=50, padx=75, highlightbackground="black", font=("Helvetica", 30, "bold"))
        self.__button_chiffrement_image.place(x=screen_width*0.5, y=screen_height*0.25, anchor="center")
        
        self.__button_masquage_image = Button(self.__root, text="Masquage image", width=20, pady=50, padx=75, highlightbackground="black", font=("Helvetica", 30, "bold"))
        self.__button_masquage_image.place(x=screen_width*0.5, y=screen_height*0.50, anchor="center")
        
        self.__button_masquage_texte = Button(self.__root, text="Masquage texte", width=20, pady=50, padx=75, highlightbackground="black", font=("Helvetica", 30, "bold"))
        self.__button_masquage_texte.place(x=screen_width*0.5, y=screen_height*0.75, anchor="center")
        
        self.__root.mainloop()
        
Interface(1440, 900)