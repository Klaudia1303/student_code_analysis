x=input ('inserisci una stringa non vuota: ')
y=0
X=x[::-1]
for i in range(len(x)):
    if x[i]==X[i]:
        y=i+1
    else:
        break
print(y)
