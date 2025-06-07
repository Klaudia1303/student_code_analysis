#trova la parola che contiene 'c' e 'a' e stampa quante stringhe sono state lette per trovarlo

s = input("stringa = ")

stringhe = 0

while s.find("a")== -1 or  s.find("c")== -1:
    stringhe = stringhe + 1
    s = input("prossima = ")

print(stringhe+1)

 
        
    
