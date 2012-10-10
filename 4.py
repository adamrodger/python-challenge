import urlgrabber, re

calcnum = 12345
print "Starting with", calcnum

for x in range(0,400):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d" % calcnum
    
    result = urlgrabber.urlread(url)
    print x, result

    try:
        calcnum = int(re.search("[0-9]+$", result).group(0))
    except:
        calcnum /= 2
