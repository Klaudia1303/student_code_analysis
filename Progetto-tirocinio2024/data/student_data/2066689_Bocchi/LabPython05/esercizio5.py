s= input('stringa: ')
n= int(input('intero positivo: '))
x=0
ris= False

for i in range(len(s)):
    if s.count(s[x])>1:
        pos1 = s.find(s[x])
        pos2 = pos1 + n
        if s[pos1] == s[pos2]:
            ris = True
    x= x+1
print(ris)
