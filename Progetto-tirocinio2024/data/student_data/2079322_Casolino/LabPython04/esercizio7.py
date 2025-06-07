s = input('Inserire una stringa: ')
i = 0
contatore_carattere = 0
while i < len(s):

    #contatore < lunghezza della stringa perchè la controllo dal primo
    #carattere fino all'ultimo, quando arrivo al numero che corrisponde
    #ad un carattere in più dell'ultimo della stringa (ovvero non esiste)
    #esce dal ciclo
    
    if s.count(s[i]) >= contatore_carattere:

        #controllo ogni carattere partendo dalla posizione 0 che ha imposto
        #il contatore e conto quante volte è ripetuto nella stringa
        
        contatore_carattere = s.count(s[i])
        carattere_max = i

        #se >= a 0 rinomino il contatore di quel particolare carattere
        #e rinomino anche il carattere
        
    i += 1

    #aggiungo 1 ad i per controllare il carattere successivo della stringa
    
print('Il carattere maggiormente presente è: ',s[carattere_max])
