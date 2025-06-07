s1=input("inserisci una stringa: ")
s2=input("inserisci un'altra stringa: ")
ris=""
for i in range(len(s1)):
    if s2.find(s1[i])==-1:
        ris=ris+s1[i]
print(ris)
