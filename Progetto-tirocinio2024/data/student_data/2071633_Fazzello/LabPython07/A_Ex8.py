##Scrivere una funzione che prende in ingresso due stringhe s1 e s2 e restituisce il prefisso
##più lungo comune alle due stringhe. Ad esempio, se s1 è ‘amaca’ e s2 è ‘amaranto’, la funzione deve
##restituire la stringa ‘ama’. Se invece, s1 è ‘amaca’ e s2 è ‘stringa’ la funzione deve restituire la stringa
##vuota ‘‘. Se (almeno) una delle due stringhe è vuota la funzione deve restituire ‘‘.

def A_Ex8(s1,s2):
    s=''
    for i in range(min(len(s2),len(s1))):
        if s1[i]==s2[i]:
            s=s+s1[i]
        else:
            break
    return s

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
