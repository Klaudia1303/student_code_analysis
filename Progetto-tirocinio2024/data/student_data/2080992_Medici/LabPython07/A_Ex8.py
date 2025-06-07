def A_Ex8(s1,s2):
    s=''
    for i in range(len(s1)):
        st=''
        c=i
        for j in range(len(s2)):
            if c>=len(s1):
                break
            if s1[c]==s2[j]:
                st+=s1[c]
                if len(st)>len(s):
                    s=st
                if j<=len(s2)-1:
                    c+=1
            else:
                if len(st)>0:
                    st=''
                    c=i
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
