import Image, re

im = Image.open("oxygen.png")
pixlist = im.load()

message = ""
for i in range(0, im.size[0], 7):
    message += chr(pixlist[i, 43][0])
    
print "".join(map(lambda x: chr(int(x)), re.findall("\d+", message)))

#integrity
