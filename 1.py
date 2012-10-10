message1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

message2 = "http://www.pythonchallenge.com/pc/def/map.html"

import sys

def decode(message):
    for x in message:
        if 97 <= ord(x) <= 120:
            sys.stdout.write(chr(ord(x) + 2))
        elif ord(x) == 121 or ord(x) == 122:
            sys.stdout.write(chr(ord(x) - 24))
        else:
            sys.stdout.write(x)
            
decode(message1)
decode(message2)