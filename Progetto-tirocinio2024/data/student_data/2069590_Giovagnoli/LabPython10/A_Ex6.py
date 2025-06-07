def A_Ex6(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    #Scrivere una funzione che riceve in input una stringa fileName, nome di un file di testo,
    #contenente in ogni riga una serie di numeri interi separati da virgole, e restituisce un dizionario che ha come
    #chiavi i numeri (in formato intero) che appaiono nel file e come valore associato a ciascuna chiave k un
    #insieme contenente i numeri di riga in cui appare k. Assumete che il numero identificativo delle righe parta
    #dal valore 1.
    f=open(fileName,encoding="UTF-8")
    d={}
    cont=1
    for riga in f:
        riga=riga.strip().split(",")
        for elem in riga:
            elem=int(elem)
            if elem in d:
                d[elem].add(cont)
            else:
                d[elem]=set()
                d[elem].add(cont)
        cont+=1
    f.close()
    return d


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['numeri1.txt'] , {10: {1,2}, -5: {1,2}, 0: {1}, 8: {2}, -3: {2}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri2.txt'] , {10: {1,2}, 0: {2}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri3.txt'] , {3: {1,2}, 4: {1}, 5: {1}, 2: {2,3}, 0: {2,3}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri4.txt'] , {2: {1,2,3,4,5}, 1: {1,2,6}, 3: {6}})
    counter_test_positivi += tester_fun(A_Ex6, ['numeri5.txt'] , {})

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)