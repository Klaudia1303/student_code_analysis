##Scrivere una funzione che prende in ingresso una lista l di stringhe e restituisce un insieme
##di tutte e sole le coppie (x,n) tali che x è una stringa di l ed n è il numero di volte che la stringa x appare
##in l. Ad esempio, se l=['jkl', 'h', 'plqa', 'jkl', 'h', 'xkj'], allora la funzione deve restituire l’insieme
##{('jkl',2), ('h',2), ('plqa',1), ('xkj',1)}. Ovviamente se la lista l in ingresso è vuota, la funzione deve
##restituire l’insieme vuoto.

def A_Ex4(l):
    st=set()
    for i in range(len(l)):
        l.count(l[i])
        x=(l[i],l.count(l[i]))
        st.add(x)
    return st

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, [['jkl', 'h', 'plqa', 'jkl', 'h', 'xkj']] , {('jkl',2), ('h',2), ('plqa',1), ('xkj',1)})
    counter_test_positivi += tester_fun(A_Ex4, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex4, [['a', 'ab', 'abc']] , {('a', 1), ('ab', 1), ('abc', 1)})
    counter_test_positivi += tester_fun(A_Ex4, [['e', 'a', 'e', 'lp', 'a', 'ql', 'cl']] ,  {('e', 2), ('a', 2), ('lp', 1), ('ql', 1), ('cl', 1)} )
    counter_test_positivi += tester_fun(A_Ex4, [['hjkl', 'hjkl']] , {('hjkl', 2)})


    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

