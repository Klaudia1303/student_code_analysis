i = 0
b = ""
c = ""
d = 0
while i == 0:
    d = d + 1 
    a = input("inserisci una stringa: ")
    if len(a) == (len(b) + len(c)):
        if d > 2:
            i = i + 1
            print(c, b, a)
    c = b
    b = a
    
