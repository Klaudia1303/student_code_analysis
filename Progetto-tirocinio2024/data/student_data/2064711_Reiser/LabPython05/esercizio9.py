l=int(input("inserisci lato del quadrato(intero dispari):"))
for i in range(l):
        if i==0 or i==l-1:
            print("*"*l)
        else:
            print("*"," "*(l-4),"*")
