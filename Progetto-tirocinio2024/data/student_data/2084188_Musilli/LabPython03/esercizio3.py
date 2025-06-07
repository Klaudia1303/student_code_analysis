n=int(input("Inserire un numero positivo o negativo \
(termina quando il numero inserito è divisibile per 5 e ridà\
 la divisione intera con l\'ultimo numero inserito): "))
while n%5!=0:
    n=int(input("Inserire un numero positivo o negativo: "))
print("\n",n//5)
    
