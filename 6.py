from zipfile import ZipFile
import re

zip = ZipFile("channel.zip")
filename = "90052.txt"
comments = []

for x in range(len(zip.infolist())):
    line = zip.open(filename).read()
    comments.append(zip.getinfo(filename).comment)
    print filename, line
    
    match = re.search("[0-9]+$", line)
    
    if not match:
        break
    else:
        filename = match.group(0) + ".txt"

print "".join(comments)

#oxygen
