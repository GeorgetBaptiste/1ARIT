from PIL import Image
from random import randint
    
class MasquageImage:


    def chiffrer_dechiffrer(self, name_image, name_key_image, key, type):
        """Chiffre ou déchiffre une image à l'aide d'une autre image qui sert de clé
        uniquement si les deux images font la même taille.

        Args:
            name_image (str): chemin de l'image à chiffrer/déchiffrer
            name_key_image (str): chemin de l'image qui sert de clé
            key (int): clé strictement positive
            type (str): "chiffrer" ou "déchiffrer"
        """
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
            key = abs(key)
            for x in range(width_image):
                for y in range(height_image):
                    r1, g1, b1 = name_image.getpixel((x, y))
                    r2, g2, b2 = name_key_image.getpixel((x, y))
                    r3, g3, b3 = self.algo(type, r1, r2, key), self.algo(type, g1, g2, key), self.algo(type, b1, b2, key)
                    pixel_map[x, y] = (r3, g3, b3)
                    pixel_count+=1
                    print("Conversion: ("+str(pixel_count)+"/"+str(width_image*height_image)+")")
            encrypted_image.save("image/output_image.bmp")
        else:
            print("L'image et la clé ne font pas la même taille.")
    
    def algo(self, type, val1, val2, key):
        """Algo de pour chiffrer/déchiffrer

        Args:
            type (str): "chiffrer" ou "déchiffrer"
            val1 (int): valeur de l'imgage
            val2 (int): valeur de l'image clé
            key (int): clé

        Returns:
            int: résultat de l'algo
        """
        if type == "chiffrer":
            val3 = round(val2+1/key*val1)
            if val3 > 255:
                val3 = 255
        elif type == "déchiffrer":
            val3 = key*(val1-val2)
        return val3
    
test = MasquageImage()
test.chiffrer_dechiffrer("image/cipher2.bmp", "image/key2.bmp", 64, "déchiffrer")