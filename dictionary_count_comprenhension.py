counts={'a':10,'b':1,'c':22}
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )