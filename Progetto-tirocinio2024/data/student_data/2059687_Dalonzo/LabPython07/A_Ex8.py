def A_Ex8(s1,s2):
    param = ''
    pos = -1
    res = ''
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    for i in range(len(s1)):
        caratt = s1[i]
        for c in range(pos + 1,len(s2)):
            if(caratt == s2[c] and c == pos + 1):
                if(ord(caratt) == 32):
                    param += ' '
                    #print('Aggiungo ' + str(ord(caratt)))
                else:
                    param += caratt
                pos = c
                #print('Aggiungo ' + str(ord(caratt)))
            elif(len(res) < len(param)):
                res = param
    if(len(res) < len(param)):
            res = param   
        
    return res



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
