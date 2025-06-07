#A_Ex2(file): Scrivere una funzione che prende in ingresso il nome di un file di testo contenente solo 
#caratteri alfabetici, spazi e carattere newline (‘\n’), e restituisce un dizionario con chiave le parole presenti 
#nel file e valore l’insieme delle righe in cui la parole compare, assumete che la numerazione delle righe 
#parta dalla riga 1. Se il file contiene:
#tanto va la gatta al lardo che ci lascia lo zampino
#tanto va la gatta
#lascia lo zampino
#Allora la funzione deve restituire: {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2}, 'al': {1}, 'lardo': 
#{1}, 'che': {1}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3}}
def A_Ex2(file):
    fin=open(file,encoding='UTF-8')
    righe=[]
    risultato={}
    a=[]
    i=0
    for riga in fin:
        righe.append(riga.strip().split())
    for frase in righe:
        i+=1
        for parola in frase:
            if parola not in risultato:
                risultato[parola]=set()
                risultato[parola].add(i)
            elif parola in risultato and parola not in a:
                risultato[parola].add(i)
            a.append(parola)
        a=[]
    return (risultato)
        
        
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
     
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex2, ['testo1.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2}, 'al': {1}, 'lardo': {1}, 'che': {1}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3}})
    counter_test_positivi += tester_fun(A_Ex2, ['testo2.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'al': {1}, 'lardo': {1}, 'che': {1}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3, 4}})
    counter_test_positivi += tester_fun(A_Ex2, ['testo3.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3, 4}})
    counter_test_positivi += tester_fun(A_Ex2, ['testo4.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1}, 'zampone': {3}, 'zampina': {4}})
    counter_test_positivi += tester_fun(A_Ex2, ['testo5.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1}, 'zampone': {3, 6}, 'zampina': {4}, 'palla': {5}})

    print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
