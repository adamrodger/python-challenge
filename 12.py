f = open("evil2.gfx", "rb")

one = open("12-1.jpg", "wb")
two = open("12-2.jpg", "wb")
three = open("12-3.jpg", "wb")
four = open("12-4.jpg", "wb")
five = open("12-5.jpg", "wb")

bytes = f.read(5)
while bytes:
    one.write(bytes[0])
    two.write(bytes[1])
    three.write(bytes[2])
    four.write(bytes[3])
    five.write(bytes[4])
    
    bytes = f.read(5)
    
one.flush()
two.flush()
three.flush()
four.flush()
five.flush()

one.close()
two.close()
three.close()
four.close()
five.close()

#disproportional