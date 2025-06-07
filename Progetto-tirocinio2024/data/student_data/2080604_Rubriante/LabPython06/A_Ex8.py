s1=input("Inserisci una stringa: ")
s2=input("Inserisci un'altra stringa: ")
n=int(input("Inserisci un numero: "))
ris=""
k=0
for i in range(0,len(s1)):
    if s2.count(s1[i])>0:
        if i+n>len(s2):
            k=len(s2)-1
        for j in range(i-n,k):
            if s2.count(s1[i])>0:
                ris=ris+s1[i]
                print(ris)
print(ris)
