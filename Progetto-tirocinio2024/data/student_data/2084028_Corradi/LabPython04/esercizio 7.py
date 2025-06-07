x=input('stringa')
i=0
z=0
while i<len(x)-1:
    if x.count(x[i])> x.count(x[i+1]):
        z=x[i]
    i=i+1
print(z)
