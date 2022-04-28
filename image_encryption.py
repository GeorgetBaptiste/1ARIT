from PIL import Image

class ImageEncryption:
    
    def __init__(self, input_image):
        self.__input_image = input_image # Fichier de l'image qu'on veut chiffrer
        self.__image = Image.open(self.__input_image) # L'image qu'on veut chiffrer avec PIL
        self.__pixel_map = self.__image.load() # Pixel map de l'image qu'on veut chiffrer
        self.__width_and_height = self.__image.size()
        self.__width = self.__width_and_height[0] # Largeur de l'image qu'on veut chiffrer
        self.__height = self.__width_and_height[1] # Hauteur de l'image qu'on veut chiffrer