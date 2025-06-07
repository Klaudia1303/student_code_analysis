def A_Ex8(s1,s2):
    y=''
    if len(s1)==0 or len(s2)==0:
        y=''
    if len(s1)>len(s2):
        for i in range(len(s2)):
            Ss1=s1[i]
            Ss2=s2[i]
            if Ss1==Ss2:
                y+=Ss1
            else:
                break
    else:
        for i in range(len(s1)):
            Ss1=s1[i]
            Ss2=s2[i]
            if Ss1==Ss2:
                y+=Ss1
            else:
                break
        
        
    return y

        


    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


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
