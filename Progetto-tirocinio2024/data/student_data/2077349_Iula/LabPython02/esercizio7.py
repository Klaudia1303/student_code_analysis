n1=int(input("Inserisci primo numero: "))
n2=int(input("Inserisci secondo numero: "))
n3=int(input("Inserisci terzo numero: "))
if n1>=n2:
    if n2>=n3:
        print("",n1,"\n",n2,"\n",n3)
    elif n1>=n3:
        print("",n1,"\n",n3,"\n",n2)
    else:
        print("",n3,"\n",n1,"\n",n2)
else:
    if n1>=n3:
        print("",n2,"\n",n1,"\n",n3)
    elif n3>=n2:
        print("",n3,"\n",n2,"\n",n1)
    else:
        print("",n2,"\n",n3,"\n",n1)
        
        
        
