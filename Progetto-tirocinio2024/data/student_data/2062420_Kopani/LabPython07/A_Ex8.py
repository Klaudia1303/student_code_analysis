def A_Ex8(s1,s2):
    s=''
    a=min(len(s1),len(s2))
    k=int(0)
    if s1=='' or s2=='':
        return s
    for i in range(a):
        if s1[:i+1]==s2[:i+1]:
            if len(s1[:i+1])>k:
                k=len(s1[:i+1])
                s=s1[:i+1]
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
