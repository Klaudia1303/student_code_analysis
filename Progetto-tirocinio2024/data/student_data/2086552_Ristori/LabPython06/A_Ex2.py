s=str(input("Inseire stringa per il calcolo del lviello della palindromicità:"))
livello=0
j=1
for i in range (0,len(s)):
    index=s[i]
    confrontare=s[len(s)-j]
    if index==confrontare:
        livello=livello+1
    j=j+1
if livello==len(s):
    print("Il livello della parola palindroma è:",(livello))
else:
    livello=int(livello/2)
    print("Il livello della parola palindroma è:",(livello))

    
