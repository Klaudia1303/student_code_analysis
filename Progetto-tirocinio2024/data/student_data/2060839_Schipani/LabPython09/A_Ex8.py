def A_Ex8(fileName):
    f=open(fileName,encoding='UTF-8').readlines()
    Riga=1
    k=0
    for riga in f:
        riga=riga.strip().split()
        x=0
        for s in riga:
            for car in s:
                if car.isupper()==True:
                    x+=1
                    if x>=k:
                        k=x
                        RIGA=Riga
        Riga+=1
    return RIGA
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
