def A_Ex8(s1,s2):
    stringa=''
    

    if len(s1)==0 or len(s2)==0:
        print(stringa)
        return(stringa)

    #while len(s1)<len(s2):
        #s1+='0'
    while len(s2)<len(s1):
        s2+='0'

    #print(s1, s2)

    for i in range(len(s1)):
        if s1[i]==s2[i]:
            stringa+=s1[i]
            #print(stringa)
        if s1[i]!=s2[i]:
            break
    return(stringa)
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
