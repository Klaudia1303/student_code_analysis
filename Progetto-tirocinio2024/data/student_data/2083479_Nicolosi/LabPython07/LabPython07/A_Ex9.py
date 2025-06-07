def A_Ex9(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    lista=[]
    for c in range(len(l)):
        s=l[c]
        massimo=0
        i=0
        while i<len(s):
            count=s.count(s[i])
            if count>massimo:
                massimo=count
                carattere_freq=s[i]
            elif count==massimo:
                if ord(s[i])<ord(carattere_freq):
                       carattere_freq=s[i]
            i+=1
        lista.append(carattere_freq)
    return lista
                
        
                
            
                
       
            
    
  
            
                
                

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, [['amaca','amaranto','rosso']], ['a','a','o'])
    counter_test_positivi += tester_fun(A_Ex9, [['osso','assolato','alto']], ['o','a','a'])
    counter_test_positivi += tester_fun(A_Ex9, [['stringa','a','bbbbcccc','dado']], ['a','a','b','d'])
    counter_test_positivi += tester_fun(A_Ex9, [['fosso','dosso','rosso','fosso']], ['o', 'o', 'o', 'o'])
    counter_test_positivi += tester_fun(A_Ex9, [['ciao mamma','ciao ']], ['a', ' '])

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
