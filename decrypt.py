from PIL import Image
class Decrypt():
    def __init__(self, image_location):
        self.binary = ""
        self.image = self.load(image_location)
        self.decrypt()
    def load(self, image_location):
        image = Image.open(image_location, "r")
        return image.convert("RGB")
    def decrypt(self):
        for pixel in self.image.getdata():
            if pixel == (0, 0, 0):
                self.binary = self.binary + "1"
            elif pixel == (255, 255, 255):
                self.binary = self.binary + "0"
        self.export(self.binary)
    def export(self, bits, encoding='utf-8', errors='surrogatepass'):
        n = int(bits, 2)
        print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0')
Decrypt("converted.png")
