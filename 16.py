from PIL import Image

im = Image.open("mozart.gif")
new = Image.new(im.mode, im.size)
pix = im.load()

offsets = []

print "Processing", im.size

#search for first purple pixel on each line
for y in range(im.size[1]):
    for x in range(im.size[0]):
        if pix[x,y] == 195:
            offsets.append(x)
            break

#shift the whole line left so the first pixel is the first purple pixel
for y, delta in enumerate(offsets):
    for x in range(im.size[0]):
        if x+delta < im.size[0]:
            new.putpixel((x,y), pix[x+delta, y])
        else:
            new.putpixel((x,y), pix[x+delta-im.size[0], y])
        
new.show()
#romance