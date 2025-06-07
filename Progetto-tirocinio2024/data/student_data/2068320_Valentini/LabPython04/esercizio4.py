n = int(input("Inserire un numero n : "))
somma = 0
while n!=0:
    if n%3==0:
        somma = somma + n
    n = int(input("Inserire un numero n : "))
print("La somma dei valori divisibili per 3 è "+str(somma))
