def A_Ex5(s,n):
    d={}
    sv=s.split()
    for i in range(len(sv)):
        t=0
        if sv[i][0] not in d:
            if len(sv[i])>=int(n):
                   d[(sv[i][0])]=[1]
                   for j in range(len(sv)):
                       if sv[j][0]==sv[i][0] and len(sv[j])>=n:
                           t+=1
                           d[sv[i][0]]=t
    return d
                        
            
            
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['tanto va la gatta al lardo che ci lascia lo zampino',3] , {'t': 1, 'g': 1, 'l': 2, 'c': 1, 'z': 1})
    counter_test_positivi += tester_fun(A_Ex5, ['tanto va la gatta al lardo che ci lascia lo zampino',5] , {'t': 1, 'g': 1, 'l': 2, 'z': 1})
    counter_test_positivi += tester_fun(A_Ex5, ['scrivere una funzione che prende in ingresso una stringa s composta di caratteri alfabetici e spazi bianchi e restituisce una lista con tutte le parole diverse della stringa',5] , {'s': 4, 'f': 1, 'p': 2, 'i': 1, 'c': 2, 'a': 1, 'b': 1, 'r': 1, 'l': 1, 't': 1, 'd': 2})
    counter_test_positivi += tester_fun(A_Ex5, ['calcoli il dizionario che ha come chiavi le lettere minuscole e come valore il numero di parole di s che cominciano per quella lettera e sono lunghe almeno n caratteri',3] , {'c': 8, 'd': 1, 'l': 3, 'm': 1, 'v': 1, 'n': 1, 'p': 2, 'q': 1, 's': 1, 'a': 1})
    counter_test_positivi += tester_fun(A_Ex5, ['',2] , {})

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
