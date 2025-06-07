def A_Ex8(fileName):
    f=open(fileName,encoding="UTF-8")
    l=f.readlines()
    countmax=0
    nmax=0
    for n in range(len(l)):
        COUNT=0
        for c in l[n]:
            if c.isupper():
               COUNT+=1
        if COUNT>=countmax:
            countmax=COUNT
            nmax=n+1
    f.close()
    return nmax
 
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
