from PIL import Image

class MasquageTexte:
    
    def masquage(self, image, texte):
        list_bin = ""
        for lettre in range(len(texte)):
            list_bin += self.str_to_bin(texte[lettre])
        image = Image.open(image)
        pixel_map = image.load()
        height = image.height
        width = image.width
        i = 0
        for y in range(height):
            for x in range(width):
                rgb = list(image.getpixel((x, y)))
                if rgb[0] == 255:
                    rgb[0] = 254
                if rgb[1] == 255:
                    rgb[1] = 254
                if rgb[2] == 255:
                    rgb[2] = 254
                for z in range(len(rgb)):
                    if i < len(list_bin):
                        rgb[z] += int(self.str_to_bin(chr(rgb[z]))[-1])^int(list_bin[i])
                    i+=1
                pixel_map[x, y] = tuple(rgb)
        image.save("image/output.bmp")
                
    def str_to_bin(self, string):
        nb = ord(string)
        list_bin = str(bin(nb))
        list_bin = list_bin[2:]
        while len(list_bin) != 8:
            list_bin = "0"+list_bin
        return list_bin
        
    def demasquage(self, image):
        image = Image.open(image)
        width = image.width
        height = image.height
        list_bin = ""
        for y in range(height):
            for x in range(width):
                r, g, b = image.getpixel((x, y))
                rgb = [r, g, b]
                for z in range(len(rgb)):
                    if rgb[z]%2 == 1:
                        list_bin += "1"
                    else:
                        list_bin += "0"
        print(self.bin_to_str(list_bin))
                        
    def bin_to_str(self, list_bin):
        x, y = 0, 8
        texte = ""
        while y <= len(list_bin) and len(texte)<1000:
            byte = list_bin[x:y]
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

test = MasquageTexte()
test.masquage("image/test.bmp", "Paul-Etienne est un connard. C'est pas Baptiste qui a écrit ce message.")
test.demasquage("image/output.bmp")