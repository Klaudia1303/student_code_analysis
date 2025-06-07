s1 = input('inserisci una stringa: ')
s2 = input('inserisci una stringa: ')
seq = '' #memorizza la sequenza
massimo = 0 #memorizza la lunghezza massima della sequnza
maxSeq = '' #memorizza la sequenza massima

for i in range(len(s1)):
    for c in range(i,len(s1)):
        seq = s1[i:c]#sequenza costruita dai for
        if(seq in s2 and len(seq)>= massimo):
            maxSeq = seq
            massimo = len(seq)
print(maxSeq)
        
          
         
            
        
        
