def A_Ex7(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    #Scrivere una funzione che prende in ingresso un file di testo contenente solo lettere alfabetiche,
    #spazi, cifre e caratteri newline (‘\n’) e restituisce la somma dei numeri presenti nel file. Ad esempio, se il file contiene:
    # Paolo è andato a casa 3 volte
    # ed ha mangiato 11 ciambelle ed una TORTA
    #Allora il risultato è 14 (3+11) visto che questi sono i soli numeri presenti nel file

    f=open(fileName,encoding="UTF-8")
    
    numeri=[]
    for righe in f:
        righe=righe.strip().split()
        for elem in righe:
            if elem.isdigit():
                numeri.append(int(elem))


    somma=sum(numeri)
    return somma

    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, ["file1.txt"] , 14)
    counter_test_positivi += tester_fun(A_Ex7, ["file2.txt"] , 17)
    counter_test_positivi += tester_fun(A_Ex7, ["file3.txt"] , 18)
    counter_test_positivi += tester_fun(A_Ex7, ["file4.txt"] , 20)
    counter_test_positivi += tester_fun(A_Ex7, ["file5.txt"] , 0)

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
