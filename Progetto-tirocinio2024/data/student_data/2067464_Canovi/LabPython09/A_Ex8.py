def A_Ex8(fileName):
    f = open(fileName, encoding = "UTF-8")
    count = 0
    numRiga = 0
    indice = 0
    for riga in f.readlines():
        indice = indice + 1
        c = 0
        a = riga.strip()
        for i in range(len(a)):
            if ord("A") <= ord(a[i]) <= ord("Z"):
                c = c + 1
        if c > count:
            count = c
            numRiga = indice
        elif c == count:
            if i > numRiga:
                count = c
                numRiga = indice
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
