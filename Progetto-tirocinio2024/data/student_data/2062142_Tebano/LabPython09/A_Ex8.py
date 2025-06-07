def A_Ex8(fileName):
    f=open(fileName)
    indice=0
    somma=0
    max_somma=0
    indice_max=0
    for riga in f:
        indice=indice+1
        for lettera in riga:
            somma=0
            if ord('A')<=ord(lettera)<=ord('Z'):
                somma=somma+1
            if somma>=max_somma:
                max_somma=somma
                indice_max=indice
    f.close()            
    return indice_max            
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
