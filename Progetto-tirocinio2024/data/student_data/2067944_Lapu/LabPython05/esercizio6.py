x=input("inserisci una stringa: ")
max=0
for i in range(len(x)):
    distanza=x.rfind(x[i])-i
    print(x[i],distanza)
    if distanza>max:
        max=distanza
print(max)
