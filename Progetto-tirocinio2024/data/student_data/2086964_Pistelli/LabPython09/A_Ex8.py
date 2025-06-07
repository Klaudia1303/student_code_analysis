def A_Ex8(fileName):
    f=open(fileName,encoding='UTF-8')
    riga=f.readline()
    x=0
    a=1
    y=1
    for riga in f:
        for elem in riga:
            for j in elem:
                if j.isalpha() and j.isupper():
                    x+=1
        if x>=y:
            y+=x
            a+=1
    f.close()
    return a

 
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
