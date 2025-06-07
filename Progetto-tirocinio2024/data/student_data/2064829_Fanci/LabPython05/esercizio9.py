l = int(input("inserisci lato del quadrato: "))
if l%2==0 or l<3:
    print("impossibile stampare quadrato")
else:
    for i in range(l):
        if i==0 or i==l-1:
            print("*"*l)
        else:
            print("*"+" "*(l-2)+"*")
 

