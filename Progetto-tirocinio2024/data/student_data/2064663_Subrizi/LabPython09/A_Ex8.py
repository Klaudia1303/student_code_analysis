def A_Ex8(fileName):
    f=open(fileName,'r',encoding='UTF-8')
    s=f.readlines()

    massimo=0
    riga=1
    r_max=1
    for elem in s:
        counter=0
        if elem.isupper():
            counter+=1
        if counter>=massimo:
            massimo=counter
            r_max=riga
        riga+=1
    f.close()
    return r_max
        
 
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
