from PIL import Image
from random import randint
    
class ImageEncryption:


    def chiffrer_dechiffrer(self, name_image, name_key_image):
        """Chiffre ou déchiffre une image à l'aide d'une autre image qui sert de clé
        uniquement si les deux images font la même taille.

        Args:
            name_image (str): chemin de l'image à chiffrer/déchiffrer
            name_key_image (str): chemin de l'image qui sert de clé
        """
        final_image = name_image
        name_image = Image.open(name_image)
        name_key_image = Image.open(name_key_image)
        width_image = name_image.width
        height_image = name_image.height
        width_key = name_key_image.width
        height_key = name_key_image.height
        if width_image == width_key and height_image == height_key:
            encrypted_image = Image.new(mode="RGB", size=(width_image, height_image))
            pixel_map = encrypted_image.load()
            pixel_count = 0
            for x in range(width_image):
                for y in range(height_image):
                    r1, g1, b1 = name_image.getpixel((x, y))
                    r2, g2, b2 = name_key_image.getpixel((x, y))
                    r3, g3, b3 = r1^r2, g1^g2, b1^b2
                    pixel_map[x, y] = (r3, g3, b3)
                    pixel_count+=1
                    print("Conversion: ("+str(pixel_count)+"/"+str(width_image*height_image)+")")
            encrypted_image.save(final_image)
        else:
            print("L'image et la clé ne font pas la même taille.")
                
                
    def create_key_image(self, name_image, width, height):
        """Créer une image qui sert de clé pour chiffrer/déchiffrer une image

        Args:
            name_image (str): chemin où l'on veut sauvegarder l'image
            width (int): taille en pixel de la largeur de l'image
            height (int): taille en pixel de la longueur de l'image
        """
        key_image = Image.new(mode="RGB", size=(width, height))
        pixel_map = key_image.load()
        for x in range(width):
            for y in range(height):
                pixel_map[x, y] = (randint(0, 255), randint(0, 255), randint(0, 255))
        key_image.save(name_image)
    
    
test = ImageEncryption()
test.chiffrer_dechiffrer("image/image1.bmp", "key/key1.bmp")