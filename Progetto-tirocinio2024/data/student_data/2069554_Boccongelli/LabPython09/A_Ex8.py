def A_Ex8(fileName):
    f = open(fileName, "r", encoding="UTF-8")
    t = f.read().split('\n')
    f.close()
    m = 0
    r = 0
    for i in range(len(t)):
        ml = 0
        for c in t[i]:
            if (c.isalpha() and c.isupper()):
                ml += 1
        if (ml >= m):
            m = ml
            r = i
    return r + 1
    
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
