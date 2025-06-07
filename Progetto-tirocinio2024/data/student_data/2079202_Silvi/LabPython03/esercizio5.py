print("questo programma restituisce il primo e l'ultimo carattere delle parole inserite\n")

i=1
inizEFine=[]
while i==1:

    s=input("inserire una parola:")
    
    if s.isalpha() and s.islower():
        
        inizEFine.append(s[0]+s[len(s)-1])
        i-=1
        
    else:
        inizEFine.append(s[0]+s[len(s)-1])


while i<=len(inizEFine)-1:

    print(inizEFine[i])
    i+=1
