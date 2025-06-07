#Scrivere una funzione che prende in ingresso una lista l di stringhe e restituisce un insieme 
#di coppie (x1, x2) tali che x1 e x2 sono stringhe di l della stessa lunghezza e x1 è diverso da x2. Notare 
#che una coppia è semplicemente una tupla di lunghezza due. In altri termini, l’insieme deve contenere 
#tutte e sole le coppie formate combinando a due a due, in tutti i possibili modi, le stringhe di l che 
#hanno la stessa lunghezza, escludendo i casi in cui una stringa si combina con se stessa. Ad esempio, 
#se l=['jkl', 'h', 'plqa', 'a', 'xkj'], allora l’insieme di coppie da restituire sarà {('jkl','xkj'), ('h','a'), ('a','h'), 
#('xkj','jkl')}. Ovviamente se la lista l in ingresso è vuota, la funzione deve restituire l’insieme vuoto.
def A_Ex3(l):
    pippo=set()
    for i in l:
        for j in l:
            if len(i)==len(j) and j!=i:
                paperopoli=j,i
                pippo.add(paperopoli)
    return pippo
                
            
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, [['jkl', 'h', 'plqa', 'a', 'xkj']] , {('jkl','xkj'), ('h','a'), ('a','h'), ('xkj','jkl')})
    counter_test_positivi += tester_fun(A_Ex3, [[]] , set())
    counter_test_positivi += tester_fun(A_Ex3, [['a', 'ab', 'abc']] , set())
    counter_test_positivi += tester_fun(A_Ex3, [['e', 'a', 'lp', 'ql', 'cl']] ,  {('e', 'a'), ('a', 'e'), ('lp', 'ql'), ('lp', 'cl'), ('ql', 'lp'), ('ql', 'cl'), ('cl', 'lp'), ('cl', 'ql')})
    counter_test_positivi += tester_fun(A_Ex3, [['hjkl', 'hjkp']] , {('hjkl', 'hjkp'), ('hjkp', 'hjkl')} )


    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
