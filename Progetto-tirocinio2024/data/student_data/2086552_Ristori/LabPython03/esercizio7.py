c=str(input("Inserie un carattere:"))
stringaIterativa=str(input("Inserie una stringa:"))
b=True
while b:
    if stringaIterativa.count(c)>2:
        print(stringaIterativa.count(c))
        b=False
    else:
        stringaIterativa=str(input("Inserie una stringa:"))
     
    
