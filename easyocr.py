import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('a2.jpeg')
for detection in result:
    print(detection[1])