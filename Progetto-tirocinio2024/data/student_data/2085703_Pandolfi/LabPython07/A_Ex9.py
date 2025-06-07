def A_Ex9(l):
    lista = []

    for x in l:
        ch = 0
        n = 1
        for y in x:
            if x.count(y) >= n:
                if ch == 0:
                    ch = ord(y)
                    n = x.count(y)
                elif x.count(y) > n:
                    n = x.count(y)
                    ch = ord(y)
                elif x.count(y) == n and ord(y) < ch:
                    n = x.count(y)
                    ch = ord(y)
        lista.append(chr(ch))

    return lista


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, [['amaca','amaranto','rosso']], ['a','a','o'])
    counter_test_positivi += tester_fun(A_Ex9, [['osso','assolato','alto']], ['o','a','a'])
    counter_test_positivi += tester_fun(A_Ex9, [['stringa','a','bbbbcccc','dado']], ['a','a','b','d'])
    counter_test_positivi += tester_fun(A_Ex9, [['fosso','dosso','rosso','fosso']], ['o', 'o', 'o', 'o'])
    counter_test_positivi += tester_fun(A_Ex9, [['ciao mamma','ciao ']], ['a', ' '])

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
