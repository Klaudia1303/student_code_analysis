def A_Ex8(fileName):
    f = open (fileName, "r", encoding = "UTF-8")
    i = 0
    massimo = 0
    indice = 0
    
    for riga in f:
        riga = riga.split(" ")
        somma = 0
        for elem in riga:
            for c in elem:
                if c.isupper():
                    somma = somma + 1
                
        if somma > massimo:
            massimo = somma
            indice = i
        elif massimo == somma and i > indice:
            indice = i
        i = i + 1
    f.close()
    return i
        
        
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
