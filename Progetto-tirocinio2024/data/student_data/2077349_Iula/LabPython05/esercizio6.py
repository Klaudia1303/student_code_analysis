s=input("Inserisci una stringa ")
distanza=0
for i in range(len(s)):
    temp=abs(s.find(s[i])-s.rfind(s[i]))
    if distanza>=temp:
        distanza=distanza
    else:
        distanza=temp
print(distanza)
