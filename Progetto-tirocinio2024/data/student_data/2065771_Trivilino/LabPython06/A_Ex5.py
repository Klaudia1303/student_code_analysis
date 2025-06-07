s=input('Inserire una stringa alfanumerica: ')
precedente='ç'  #variabile per salvare il carattere precedente della stringa
occorrenze=1
risultato=0
for i in range(0,len(s)+1):
    
    if s[i:i+1]==precedente:
        occorrenze+=1
        if occorrenze>=risultato:
            carattere=s[i:i+1] #salva il carattere con il n di occorrenze magg
            risultato=occorrenze #risultato contiene il n di occorrenze maggiori
           
    else:
        occorrenze=1
        
    precedente=s[i:i+1]
    
print(carattere)
print(risultato)
