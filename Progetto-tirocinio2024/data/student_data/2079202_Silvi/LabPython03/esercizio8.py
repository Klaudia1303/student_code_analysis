print("questo programma verifica se una stringa è palindroma e ne stampa la lunghezza\n")
i=0
z=0
while i==0:
    s=input("inserire una stringa:")
    while z<len(s):
        
        if s[z]==s[(len(s)-z-1)]:
            
            z+=1

            if z==len(s):

                print(len(s))
            
        else:
            print("non palindroma, inserire una stringa palindroma")
            z=len(s)
