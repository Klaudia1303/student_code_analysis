#A_Ex6(fileName) Scrivere una funzione che riceve in input una stringa fileName, nome di un file di testo, 
#contenente in ogni riga una serie di numeri interi separati da virgole, e restituisce un dizionario che ha come 
#chiavi i numeri (in formato intero) che appaiono nel file e come valore associato a ciascuna chiave k un 
#insieme contenente i numeri di riga in cui appare k. Assumete che il numero identificativo delle righe parta 
#dal valore 1. Ad esempio se il file contiene 
#10,-5,-5,0 
#10,-5,8,-3 
#la funzione deve restituire:
#{10: {1,2}, -5: {1,2}, 0: {1}, 8: {2}, -3: {2}}
def A_Ex6(fileName):
    fin=open(fileName,encoding='utf-8')
    righe=[]
    risultato={}
    contarighe=0
    for riga in fin:
        righe.append(riga.strip().split(','))
    for numeri in righe:
        contarighe+=1
        for numero in numeri:
            if int(numero) not in risultato:
                risultato[int(numero)]=set()
            risultato[int(numero)].add(contarighe)
    return risultato
   
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
