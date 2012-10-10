from datetime import date

for y in range(1006, 1997, 10):
    d = date(y, 1, 27)
    if d.weekday() == 1:
        print d
        
# mozart

# mozart's birthday is Tuesday 27/01/1756
