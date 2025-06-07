def A_Ex8(s1,s2):
    s3=""
    if len(s1)==0 or len(s2)==0:
        return s3
    else:
        for i in range(len(s1)):
            if i<len(s2) and i<len(s1):
                if s1[i]==s2[i]:
                    s3+=s1[i]
                else:
                    break
        return s3
        

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
