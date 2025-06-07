s = str(input('Inserire stringa s: '))
while len(s)<1:
    s = str(input('Inserire di nuovo la stringa s: '))
dismax=0
l=len(s)
for i in range(l) :
    distanza = s.rfind(s[i])-i
    if dis> dismax :
        dismax=dis
print(dismax)
