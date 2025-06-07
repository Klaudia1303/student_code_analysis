from math import *
n1=input("Inserire il primo valore: ")
n2=input("Inserire il secondo valore: ")
n3=input("Inserire il terzo valore: ")
alto=max(n1,n2,n3)
basso=min(n1,n2,n3)
if (alto==n1 and basso==n2) or (alto==n2 and basso == n1):
    medio=n3
elif (alto==n2 and basso==n3) or (alto==n3 and basso == n2):
    medio=n1
else:
    medio=n2
print("I numeri in ordine decrescente sono: "+str(alto)+","+str(medio)+","+str(basso))
