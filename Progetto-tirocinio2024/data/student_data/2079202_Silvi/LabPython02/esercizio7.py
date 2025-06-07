print("questo programma ordina in ordine decrescente 3 numeri dati in input\n")
n1=int(input("inserire primo numero:"))
n2=int(input("inserire secondo numero:"))
n3=int(input("inserire terzo numero:"))
if n1>n2:
    
    if n2>n3:
        print("\n",n1,"\n",n2,"\n",n3)
            
    else:
        if n1>n3:
            print("\n",n1,"\n",n3,"\n",n2)
        else:
            print("\n",n3,"\n",n1,"\n",n2)
        
else:
    if n3>n2:
        print("\n",n3,"\n",n2,"\n",n1)
    else:
        if n1>n3:
            print("\n",n2,"\n",n1,"\n",n3)
        else:
            print("\n",n2,"\n",n3,"\n",n1)
            
