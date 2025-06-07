s=input('Inserire una stringa (contiene "a" e "c" per terminare):' )
somma=0
while not (("a" and "c") in s):
    somma +=1
    s=input('Inserire una stringa (contiene "a" e "c" per terminare):' )
print(somma+1)
      
