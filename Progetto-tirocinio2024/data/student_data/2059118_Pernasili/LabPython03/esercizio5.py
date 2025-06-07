s = input("Inserisci una stringa: ")

while s.islower() == False or s.isalpha() == False :
    
    x = s[-len(s)]
    y = s[len(s)-1]
    print(x)
    print(y)
    s = input("Inserisci una stringa: ")
