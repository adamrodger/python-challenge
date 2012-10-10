import pickle, urllib2, sys

o = pickle.loads(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read())

for line in o:
    for option in line:
        char, count = option
        sys.stdout.write("".join([char for x in range(count)]))
    print "\n"
    
#channel
