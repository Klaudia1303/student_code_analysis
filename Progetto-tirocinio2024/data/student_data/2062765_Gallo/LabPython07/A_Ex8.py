def A_Ex8(s1,s2):
    s3=""
    s4=""
    minimo=min(len(s1),len(s2))
    if minimo!=0:
        for i in range(minimo):
            if s1[i]==s2[i]:
                s3+=s1[i]
            else:
                if len(s3)>=len(s4):
                    s4=s3
                    s3=""
        if len(s3)>=len(s4):
                    s4=s3
    return s4

s1=input("Inserisci stringa 1: ")
s2=input("Inserisci stringa 2: ")
print(A_Ex8(s1,s2))
    

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
