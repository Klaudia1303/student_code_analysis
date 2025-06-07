l=0
while l<=1:
    l=int(input('inserisci il lato del quadrato: '))
print ('*'*l)
for i in range (l-2):
    print ('*', ' '*(l-2), '*')
print ('*'*l)
