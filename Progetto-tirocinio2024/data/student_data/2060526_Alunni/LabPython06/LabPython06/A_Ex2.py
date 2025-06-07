x=input('inserisci una stringa non vuota: ')
livello=0
X=x[::-1]
for i in range (len(x)):
    if x[i]==X[i]:
        livello=i+1
    else:
        break
print(livello)
