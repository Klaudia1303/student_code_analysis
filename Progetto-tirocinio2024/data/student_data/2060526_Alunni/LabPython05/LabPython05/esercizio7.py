x=(input('inserisci una stringa:  '))
s="False"
for i in range(len(x)):
    if x.find(x[i])!= x.rfind (x[i]):
        s="True"
print(s)

