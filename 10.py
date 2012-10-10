"""
len(a[30]) = ?
"""

a = ["1", "11"]

for seqlen in range(1, 30):
    count = 1
    last = a[seqlen][0]
    newval = ""

    for c in a[seqlen][1:]:
        if c == last:
            count += 1
        else:
            newval += (str(count) + last)
            count = 1
            
        last = c
        
    newval += (str(count) + last)
    a.append(newval)
    
#print a
#print a[30]
print len(a[30]) # 5808
