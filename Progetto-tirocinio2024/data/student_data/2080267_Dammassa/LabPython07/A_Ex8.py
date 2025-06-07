def A_Ex8(s1,s2):
    stringa = ""
    if s1 == "" or s2 == "":
        return stringa
    if len(s2) < len(s1):
        for i in range(len(s2)):
          if s1[i] not in s1 or s1[i] not in s2:
                break
          if s2[i] in s1 and s2[i] in s2:
                stringa += s2[i]
    else:
        for i in range(len(s1)):
          if s1[i] not in s1 or s1[i] not in s2:
                break
          if s1[i] in s1 and s1[i] in s2:
                stringa += s1[i]
    return stringa
        

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
