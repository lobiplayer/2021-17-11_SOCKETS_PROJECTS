from PIL import Image
import os

# Image.open("2_of_clubs.png").save("test.bmp")
for filename in os.listdir("./PNG-cards-1.3"):
    print
    Image.open('./PNG-cards-1.3/' + filename).save('./PNG-cards-1.3/' + filename[:-4] + '.bmp')
