def A_Ex8(s1,s2):
    prefisso = ''
    
    if s1 == '' or s2 == '' :
        prefisso == ''
    else:
        lista1 = list(s1)#lista i caratteri della stringa
        lista2 = list(s2)

        if lista1 < lista2:
                for i in range(len(lista1)): #itera sulle posizioni dei caratteri
                        carattere1 = lista1[i] #carattere in posizione i
                        carattere2 = lista2[i]
            
                        if carattere1 == carattere2: 
                            prefisso += carattere1
                        else:
                            break #appena sono diversi ti fermi al prefisso trovato
        else:
                for i in range(len(lista2)): #itera sulle posizioni dei caratteri
                        carattere1 = lista1[i]
                        carattere2 = lista2[i]
            
                        if carattere1 == carattere2:
                            prefisso += carattere1
                        else:
                            break

    return prefisso
            
            
        
        












    


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ['amaca','amaranto'], 'ama')
    counter_test_positivi += tester_fun(A_Ex8, ['asso','assolato'], 'asso')
    counter_test_positivi += tester_fun(A_Ex8, ['','stringa'], '')
    counter_test_positivi += tester_fun(A_Ex8, ['stringa',''], '')
    counter_test_positivi += tester_fun(A_Ex8, ['ciao mamma','ciao '], 'ciao ')

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
