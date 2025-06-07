def A_Ex7(s):
    lista=[]
    if s=='':
        return lista
    else:
        for i in range(len(s)):
            if s[i].isupper()==True:
                lista+=s[i]
                lista.sort()
                for j in range(0,len(lista)-1):
                    if lista.count(lista[j])>1:
                        lista.remove(lista[j])
        return lista


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
