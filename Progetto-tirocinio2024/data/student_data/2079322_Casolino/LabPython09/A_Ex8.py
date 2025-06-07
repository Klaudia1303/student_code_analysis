def A_Ex8(fileName):
    f=open(fileName, 'r',encoding='UTF-8')
    M=0
    pos=1
    for line in f:
        conta=0
        for elem in line: #prendo elemento nella riga
            if elem.isupper():
                conta+=1
        if conta>=M:
            M=conta
            sol=pos
        pos+=1 #in questa posizione perchè il for per le righe è quello esterno
    f.close()
    return sol
 
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
