n = int(input("Inserisci un numero maggiore di 1: "))

if n > 1:
    i = 2 # primo numero da controllare
    while i <= n:
        prime = True
        if i > 1:
            j = 2 # primo divisore da controllare
            while j < i:
                if i % j == 0:
                    prime = False
                    break
                j += 1
        else:
            prime = False
        
        if prime:
            print(i)
        i += 1
