def A_Ex8(fileName):
    f = open(fileName,encoding='UTF-8')
    
    maiusc = []
    for l in f:
        maiusc.append(len([c for c in l if c.isupper()]))

    l, lm = 0, maiusc[0]
    for i in range(1, len(maiusc)):
        if maiusc[i] >= lm:
            l, lm = i, maiusc[i]
    
    f.close()
    return l+1
     
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
