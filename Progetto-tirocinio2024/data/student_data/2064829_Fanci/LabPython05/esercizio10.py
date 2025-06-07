l =  input("inserisci lato: ")
if l<2: print("impossibile stampare quadrato")
else:
    for i in range(l):
        for j in range(l):
            if i==0 or i==l:
                print("*"*l)
            else:
