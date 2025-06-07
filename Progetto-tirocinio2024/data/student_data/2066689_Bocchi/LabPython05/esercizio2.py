s= input('stringa: ')
n= int(input('numero di ripetizione: '))
x=0
ris=''
for i in range(len(s)):
    ris= ris + s[x]*n
    x= x+1
print(ris)
