n=int(input("Inserire un numero intero (0 per terminare):"))
somma=0
while n!=0:
        if n%3==0:
            somma+=n
        n=int(input("Inserire un numero intero (0 per terminare):"))
print("La somma dei numeri divisibili per 3 è:", somma)
