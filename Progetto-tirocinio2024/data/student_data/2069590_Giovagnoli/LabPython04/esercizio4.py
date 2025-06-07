n = int(input("Inserire un numero intero: "))
somma = 0
while n!=0:
    if n%3==0:
        somma += n
    n=int(input("Inserire un numero intero: "))
print("Somma dei numeri interi divisibili per 3 = ",somma)