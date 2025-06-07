n1=int(input("Inserisci un numero "))
n2=int(input("Inserisci un numero "))
n3=int(input("Inserisci un numero "))
if((n1>=n2)and(n1>=n3)):
    if(n2>=n3):
        print("\n",n1,"\n",n2,"\n",n3)
    else:
        print("\n",n1,"\n",n3,"\n",n2)
elif((n2>=n1)and(n2>=n3)):
    if(n1>=n3):
        print("\n",n2,"\n",n1,"\n",n3)
    else:
        print("\n",n2,"\n",n3,"\n",n1)
elif((n3>=n1)and(n3>n2)):
    if(n1>=n2):
        print("\n",n3,"\n",n1,"\n",n2)
    else:
        print("\n",n3,"\n",n2,"\n",n1)
