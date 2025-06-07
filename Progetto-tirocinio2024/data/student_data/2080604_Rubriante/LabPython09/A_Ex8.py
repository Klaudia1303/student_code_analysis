def A_Ex8(fileName):
    f=open(fileName,encoding="UTF-8")
    riga=0
    rigasave=0
    con=0
    consave=0
    for elem in f:
        for let in elem:
            if let.isalpha()==True and let.isupper()==True:
                con+=1
        riga+=1
        if con>consave:
            consave=con
            rigasave=riga
    return riga



    
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
