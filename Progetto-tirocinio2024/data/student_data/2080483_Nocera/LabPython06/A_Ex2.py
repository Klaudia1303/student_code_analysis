s=input("inserisci una parola :")  #il programma verifica di che livello è la stringa
sinv=s[::-1]
l=0
for i in range (len(s)//2):
    oi=sinv[i]
    ai=s[i]
    if s[i]==sinv[i]:
        l=l+1
if l==(len(s)//2):
    l=l*2
print("il livello della stringa è",l,)
    
