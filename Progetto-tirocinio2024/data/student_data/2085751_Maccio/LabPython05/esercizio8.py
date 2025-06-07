l=int(input("Inserire lunghezza del lato (numero dispari)maggiore di 3:  "))
g=int(l/2)
i=1
while l>=i:
    print(g*" "+"*"*i+g*" ")
    g=g-1
    i=i+2
