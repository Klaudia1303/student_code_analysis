def A_Ex8(fileName):
    """Scrivere una funzione che prende in ingresso un file di testo contenente solo lettere alfabetiche,
spazi, cifre e caratteri newline (‘\n’) e restituisce il numero della riga che contiene più caratteri alfabetici maiuscoli.
Se ci sono più righe con lo stesso numero, restituisca quella di indice più grande. Si assuma che la prima riga abbia
indice 1. Ad esempio, se il file è quello di sopra, allora il risultato è 2, poiché la seconda riga hanno più caratteri
alfabetici maiuscoli della 1."""


    f = open(fileName, "r", encoding= "UTF-8")
    lista=[riga for riga in f]
    posizione = 0
    counter = 0
    pos = 0
    for elem in lista:
        pos += 1
        count= 0
        for i in range(len(elem)):
            if elem[i].isupper():
                count+= 1
                if count >= counter:
                    counter = count
                    posizione = pos
    return posizione
        
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["file1.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file2.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file3.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file4.txt"] , 3)
    counter_test_positivi += tester_fun(A_Ex8, ["file5.txt"] , 3)

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
