s = str(input('Inserire stringa s: '))
while len(s)<1:
    s = str(input('Inserire di nuovo la stringa s: '))
p='False'
l=len(s)
for i in range(l) :
    presenza = s.rfind(s[i])
    
    if presenza != i :
        p='True'
print(p)
