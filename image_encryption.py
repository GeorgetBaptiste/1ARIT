from PIL import Image

class ImageEncryption:
    
    def __init__(self, input_image):
        self.__input_image = input_image # Fichier de l'image qu'on veut chiffrer
        self.__image = self.open_image() # L'image qu'on veut chiffrer avec PIL
        self.__pixel_map = self.extracting_pixel_map() # Pixel map de l'image qu'on veut chiffrer
        self.__width = self.extracting_width_height()[0] # Largeur de l'image qu'on veut chiffrer
        self.__height = self.extracting_width_height()[1] # Hauteur de l'image qu'on veut chiffrer
        self.__key_image 
        self.__encrypted_image
        
    def open_image(self):
        return Image.open(self.__input_image)
    
    def extracting_pixel_map(self):
        return self.__image.load()
    
    def extracting_width_height(self):
        return self.__image.size()