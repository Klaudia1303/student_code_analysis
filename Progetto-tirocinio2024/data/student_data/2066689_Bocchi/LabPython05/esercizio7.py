s= input('stringa: ')
x=0
ris= False

for i in range(len(s)):
    if s.count(s[x])>1:
        ris = True
    x= x+1
print(ris)
