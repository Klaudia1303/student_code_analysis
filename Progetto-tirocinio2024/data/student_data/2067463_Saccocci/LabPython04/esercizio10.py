s=input('Inserire una stringa:')
precedente=s
precedente2=s
while len(precedente)+len(precedente2)!=len(s):
     precedente=s
     s=input('Inserire una stringa:')
     precedente2=s
     s=input('Inserire una stringa:')
print(precedente+' '+precedente2+' '+s)
    

