def A_Ex9(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    listafinale=[]
    ris=0
    
    for i in range(len(l)):
        vecchio=0
        for x in range(len(l[i])):
            carattere= l[i][x]
            countCarattere= l[i].count(l[i][x])
            
            if l[i].count(l[i][x]) > vecchio:
                vecchio= l[i].count(l[i][x])
                vecchioCarattere= l[i][x]
            elif l[i].count(l[i][x]) == vecchio and ord(l[i][x]) <= ord(vecchioCarattere):
                vecchioCarattere= l[i][x]
        listafinale.append(vecchioCarattere)
        
    return listafinale

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
