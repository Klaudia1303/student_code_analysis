def A_Ex9(l):
    l1=[]
    if len(l)>0:
        for parola in l:
            ricorrenzemax=1
            letteramax='|'
            for lettera in parola:
                ricorrenze=parola.count(lettera)
                if ricorrenze>ricorrenzemax:
                    letteramax=lettera
                    ricorrenzemax=ricorrenze
                if ricorrenze==ricorrenzemax and ricorrenzemax!=1:
                    if ord(lettera)<ord(letteramax):
                        letteramax=lettera
                if ricorrenze==ricorrenzemax and ricorrenzemax==1:
                    if ord(lettera)<ord(letteramax):
                        letteramax=lettera
                    
            if letteramax!='|':
                l1.append(letteramax)
            else:
                l1.append(' ')
            
                
    return l1



    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
