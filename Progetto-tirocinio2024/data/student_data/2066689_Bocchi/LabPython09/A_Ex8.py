def A_Ex8(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    riga=[]
    f= open(fileName, encoding='UTF-8')
    for el in f:
        el=el.strip().split(',')
        riga.append(el)
    for a in range(len(riga)):
        for b in range(len(riga[a])):
            conta=0
            conta_prec=0
            for x in range(len(riga[a][b])):
                if riga[a][b][x].isupper():
                    conta += 1
                    if conta >= conta_prec:
                        conta_prec= conta
                        ris= a+1
    f.close()
    return ris
 
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
