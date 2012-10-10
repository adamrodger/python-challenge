import Image

im = Image.open("cave-odd.jpg")
im = im.resize((320,240))
im.save("cave-2.jpg")
