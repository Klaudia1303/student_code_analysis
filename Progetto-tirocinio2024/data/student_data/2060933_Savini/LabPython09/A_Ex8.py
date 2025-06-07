def A_Ex8(fileName):
    f=open(fileName,encoding='UTF-8')
    x=0
    y=0
    for c in f:
        k=''.join(c.strip().split(' '))
        l=0
        x=x+1
        for i in k:
            if i.isupper():
                l=l+1
        if l>=y:
            y=l
            s=x
    f.close()
    return s




















    





    
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
