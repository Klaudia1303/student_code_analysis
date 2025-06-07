def A_Ex8(fileName):
    r_max=0
    row=0

    with open(fileName,'r',encoding='UTF-8') as f:
        x=f.readlines()
        for elem in range(len(x)):
            alpha=0
            for word in range(len(x[elem])):
                if ord(x[elem][word])>64 and ord(x[elem][word])<91:
                    alpha+=1
                if alpha>=r_max:
                    r_max=alpha
                    row=elem+1
                    
    return row
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
