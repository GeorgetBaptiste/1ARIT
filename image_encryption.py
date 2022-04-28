from PIL import Image
    
class ImageEncryption:
    
    def __init__(self, input_image):
        self.__input_image = input_image # Fichier de l'image qu'on veut chiffrer
        self.__image = Image.open(self.__input_image) # L'image qu'on veut chiffrer avec PIL
        self.__pixel_map = self.__image.load() # Pixel map de l'image qu'on veut chiffrer
        self.__width = self.__image.width # Largeur de l'image qu'on veut chiffrer
        self.__height = self.__image.height # Hauteur de l'image qu'on veut chiffrer
        # self.__key_image 
        # self.__encrypted_image
        
    def open_image(self):
        return Image.open(self.__input_image)
    
    def extracting_pixel_map(self):
        return self.__image.load()
    
    def extracting_width_height(self):
        return self.__image.size()

    def rgb_image(self):
        for x in range(self.__width):
            for y in range(self.__height):
                r,g,b = self.__image.getpixel((x,y))
        print(str(r)+", "+str(g)+", "+str(b))

test = ImageEncryption("pomme.jpg")
test.rgb_image()