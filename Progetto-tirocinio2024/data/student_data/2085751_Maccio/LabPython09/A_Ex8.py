def A_Ex8(fileName):
    file=open(fileName,'r',encoding='UTF-8')
    f=0
    p=0
    g=0
    for riga in file:
        riga=riga.strip().split('/n')
        for i in riga:
            c=0
            g=g+1
            if i.isupper()==True and i.isalpha()==True:
                c=c+1
            if c>=p:
                p=c
                f=g
    file.close() 
    return f
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
