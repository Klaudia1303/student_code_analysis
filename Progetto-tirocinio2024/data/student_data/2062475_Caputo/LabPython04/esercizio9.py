n = int ( input ("inserire un numero intero maggiore di 0, n: "))
print ("1\n1")
somma1 = int (1)
somma2 = int (1)
while (somma1 < n and somma2 < n):
    somma1 = somma1 + somma2
    print (somma1)
    somma2 = somma1 + somma2
    print (somma2)
