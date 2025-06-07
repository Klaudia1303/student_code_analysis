def A_Ex8(fileName):
    f = open(fileName, "r")

    righe = []

    for x in f:
        righe.append(x.strip())

    f.close()

    indice = 0
    somma = 0
    somma_tmp = 0

    for y in range(len(righe)):
        for z in righe[y]:
            if z.isupper():
                somma_tmp += 1
        if somma <= somma_tmp: 
            somma = somma_tmp
            indice = y + 1 

    return indice

         

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
