def A_Ex8(s1,s2):
    maggiore=''
    for i in range(len(s1)):
        if s1[i] in s2:
            k=i
            s3=''
            for j in range(s2.find(s1[i]),len(s2)):
                if k==len(s1) or s1[k]!=s2[j]:
                    break
                else:
                    s3+=s2[j]
                    k+=1
                if len(s3)>len(maggiore):
                    maggiore=s3
    return maggiore


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
