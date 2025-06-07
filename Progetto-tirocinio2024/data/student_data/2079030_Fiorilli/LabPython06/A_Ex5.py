s=''
while s=='':
    s=input('inserisci una stringa non vuota: ')
c=1
lett=''
mass=1
for i in range (len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        c=1
    if c>=mass:
        mass=c
        lett=s[i]
if mass!=1:
    print (lett, mass)
