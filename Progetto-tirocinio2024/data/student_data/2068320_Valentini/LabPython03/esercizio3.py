n=1
resto=n%5
while resto!=0:
    n=int(input("Inserire un numero. Il programma terminerà quando si inserirà un numero divisibile per 5: "))
    resto=n%5
print(int(n)/5)
