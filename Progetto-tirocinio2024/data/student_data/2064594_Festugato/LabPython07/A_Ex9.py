def A_Ex9(l):
    risultato = []
    M = 0
    
    for stringa in l:     #itera sulle stringhe della lista

        for c in stringa: #itera sui caratteri della stringa
            numero = stringa.count(c)#conta il numerodi volte in cui compare c
            
            if numero > M:
                M = numero #salvi il numero di volte massimo di un carattere
               
                
                carattereMax = c #aggiorno il carttereMax a qullo corrente
                
                
            elif numero == M  and  ord(c) < ord(carattereMax):
                    carattereMax = c #aggiorno il carattere che devo considerare
                    
        risultato.append(carattereMax) #ogni fine stringa salvi il carattereMax


        M = 0 #riazzero il massimo alla fine di ogni stringa


    return risultato
                    
        
    
    

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
