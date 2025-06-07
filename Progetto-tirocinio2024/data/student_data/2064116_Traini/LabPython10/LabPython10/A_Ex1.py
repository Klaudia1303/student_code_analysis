#A_Ex1(l): Scrivere una funzione che riceve in ingresso una lista l di stringhe e restituisce il dizionario in 
#cui le stringhe di l sono le chiavi ed il valore associato a ciascuna chiave k è il numero di volte in cui la 
#stringa k compare nella lista. Se la lista l in ingresso è vuota, la funzione deve restituire il dizionario vuoto 
#{}. Ad esempio, se l=['casa','orso','cane','casa','orso','casa'] allora il dizionario 
#restituito sarà {'casa': 3, 'orso': 2, 'cane': 1}. Notate che l’ordine per i dizionari non è 
#rilevante
def A_Ex1(l):
    d={}
    for elem in l:
        h=(l.count(elem))
        if elem not in d:
            d[elem]=h
    return d
    
        
        
    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, [['casa','orso','cane','casa','orso','casa']] , {'casa': 3, 'orso': 2, 'cane': 1})
    counter_test_positivi += tester_fun(A_Ex1, [['casa','casa','casa']] , {'casa': 3})
    counter_test_positivi += tester_fun(A_Ex1, [['casa','orso','cane','cassa','osso','casta']] , {'casa': 1, 'orso': 1, 'cane': 1, 'cassa': 1, 'osso': 1, 'casta': 1})
    counter_test_positivi += tester_fun(A_Ex1, [['casa']] , {'casa': 1})
    counter_test_positivi += tester_fun(A_Ex1, [[]] , {})

    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
