def A_Ex8(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f = open(fileName)
    lettura = f.readlines()
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    conta = 0
    conta_max = 0
    riga = 1
    for i in range(len(lettura)):
        for k in range(len(alfabeto)):
            if alfabeto[k] in lettura[i]:
                conta = conta + lettura[i].count(alfabeto[k])
        if conta > conta_max:
            conta_max = conta
            riga = i + 1
    return(riga)
                
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
