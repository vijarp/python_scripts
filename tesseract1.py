import pytesseract as pt
import os
from PIL import Image
path1 = "e:\\biodatas\\new\\"


for file in os.listdir(path1):
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        basename = os.path.splitext(os.path.basename(file))
        base1 = basename[0]
        img = Image.open(path1 + file)
        r = pt.image_to_string(img)
        f1 = open(path1 +'\\txts\\'+base1+".txt","w")
        f1.write(r)
        f1.close()
