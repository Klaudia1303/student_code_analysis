def A_Ex2(l):
     if not l:
          return set()
     
     # chars è una lista di set contenti ognuno i caratteri che figurano almeno due volte
     # in ogni stringa della lista
     chars = []
     for w in l:
          chars.append(set([c for c in w if w.count(c) >= 2]))
     
     # viene restituita l'unione dei set 
     return set().union(*chars)

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex2, [['casa', 'albero', 'bello']] , {'a','l'})
    counter_test_positivi += tester_fun(A_Ex2, [['ciao', 'ciao']] , set())
    counter_test_positivi += tester_fun(A_Ex2, [['aa','aa','hghjklhl']] , {'a','h','l'})
    counter_test_positivi += tester_fun(A_Ex2, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex2, [['cogito', 'ergo', 'sum']] , {'o'})


    print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
