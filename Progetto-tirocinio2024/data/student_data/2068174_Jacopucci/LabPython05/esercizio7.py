s = str(input('Inserire stringa s: '))
while len(s)<1:
    s = str(input('Inserire di nuovo la stringa s: '))
p='False'
l=len(s)
for i in range(l) :
    pres=s.rfind(s[i])
    
    if pres!=i:
        p='True'
print(p)
