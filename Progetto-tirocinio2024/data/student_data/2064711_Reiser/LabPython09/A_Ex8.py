def A_Ex8(fileName):
    f=open(fileName,encoding='UTF-8')
    s=f.read().strip().split('\n')
    conta=0
    a=0
    for riga in s:
        for j in riga:
            for car in j:
                if car.isupper()==True:
                    conta+=1
        if conta>=a:
            a=conta
            rigaris=s.index(riga)+1
    conta=0
    return rigaris
    f.close()
 
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
