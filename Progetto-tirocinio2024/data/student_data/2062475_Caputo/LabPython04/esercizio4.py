n = int ( input ("inserire il numero n: "))
somma = 0
while n != 0:
    if ( n%3 == 0):
        somma = somma + n
    n = int ( input ("inserire il numero n, oppure 0 per terminare: "))
print ("la somma dei numeri interi positivi inseriti divisibili per tre è:", somma)
