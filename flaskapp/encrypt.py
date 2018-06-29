from PIL import Image
import math, os
class Encrypt():
    def __init__(self, text, filename, file_format):
        self.filename = filename
        self.file_format = file_format
        self.binary = self.text_to_bits(text)
        self.size = int(round(math.sqrt(len(self.binary))))
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)
        self.image = Image.new("RGB", (self.size, self.size), self.white)
        self.encrypt()
    def text_to_bits(self, text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))
    def encrypt(self):
        count = 0
        for y in range(self.size):
            for x in range(self.size):
                if count < len(self.binary):
                    if self.binary[count] == "0":
                        self.image.putpixel((x, y), self.white)
                    else:
                        self.image.putpixel((x, y), self.black)
                    count+=1
                else:
                    self.image.putpixel((x, y), self.blue)
        self.export()
    def export(self):
        try:
            self.image.save(self.filename + "." + self.file_format, self.file_format)
            print("Done!")
        except:
            print("Error saving file.")
os.system("clear")
Encrypt(
    input("Enter some plaintext: "),
    "converted",
    "png"
)
