s1=input("Inserisci una sringa: ")
s2=input("Inserisci un'altra stringa: ")
ris=""
for i in range(0,len(s1)+1):
    for j in range(i+1,len(s1)+1):
        if s2.count(s1[i:j])>0:
            if len(ris)<len(s1[i:j]):
                ris=s1[i:j]
print(ris)
