#Ex6(file): scrivere una funzione Python che, preso in ingresso il nome di un file di testo calcoli, usando le 
#espressioni regolari, quante volte compare una parola con la seguente proprietà:
#“la lettera iniziale e finale della parola sono uguali ed 
#all’interno della parola compare almeno una doppia.”
#Si noti che la doppia deve comparire all’interno della parola, senza quindi considerare il primo e l’ultimo 
#carattere della parola stessa. Ad esempio, prendendo come input il file contenente il seguente testo: 
#tanto attacca contro elettore in giro abbastanza era andato a casa
#la funzione deve restituire come risultato 3.
import re
def Ex6(file):
    dossier=open(file,encoding='utf-8')
    read=dossier.read()
    pattern=r'\b\w*(\w)\w*(\w)\2\w*\1\w*\b'
    ris=re.findall(pattern,read,re.IGNORECASE)
    return len(ris)
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex6, ["file3_1.txt"] , 3)
    counter_test_positivi += tester_fun(Ex6, ["file3_2.txt"] , 3)
    counter_test_positivi += tester_fun(Ex6, ["file3_3.txt"] , 2)
    counter_test_positivi += tester_fun(Ex6, ["file3_4.txt"] , 4)
    counter_test_positivi += tester_fun(Ex6, ["file3_5.txt"] , 4)

    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
