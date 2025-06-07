n = int (input ("iserire il numero n: "))
somma = 0
while n != '*':
    n = input ("inserire il numero n, oppure * per terminare: ")
    if ('-' not in n):
        somma = somma + 1
print ("il numero di interi positivi inseriti è:", somma)
