def A_Ex7(s):
    
    resList=[]
    uniList=[]
    for check in s:
        if check.isupper()==True:
            if check not in resList:
                resList.append(check)
    for letter in resList:
        uniList.append(ord(letter))
    uniList.sort()
    resList.clear()
    for finalCheck in uniList:
        resList.append(chr(finalCheck))
    return resList

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, ['cIAo MAmMa'],['A','I','M'])
    counter_test_positivi += tester_fun(A_Ex7, ['3219'], [])
    counter_test_positivi += tester_fun(A_Ex7, ['aG2Hl'], ['G','H'])
    counter_test_positivi += tester_fun(A_Ex7, ['PPq&/&90PQ'], ['P','Q'])
    counter_test_positivi += tester_fun(A_Ex7, [''], [])

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
