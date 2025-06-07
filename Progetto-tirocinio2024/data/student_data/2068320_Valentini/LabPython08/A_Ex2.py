def A_Ex2(l):
     """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
     if l == []:
          return(set())
     else:
          lista = []
          for i in range(97 ,122):
               for k in range(len(l)):
                    conta = l[k].count(chr(i))
                    if conta >= 2:
                         lista.append(
                              chr(i))
                         break
          return(set(lista))
          
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
