s=input("Inserisci una stringa (termina inserendo tutti caratteri minuscoli)")
while str.islower(s)==False or str.isalpha(s)==False:
    print(s[0],s[-1])
    s=input("Inserire una stringa")
print(s[0],s[-1])
        
        
