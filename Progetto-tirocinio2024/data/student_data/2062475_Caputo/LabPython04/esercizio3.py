n = input ("inserire il numero n: ")
somma = 0
while n != '*':
    if ( '-' in n):
        n = int (n)
        somma = somma + n
    n = input ("inserire un numero n, oppure * per terminare: ")
print ("la somma dei numeri interi negativi è:", somma)
