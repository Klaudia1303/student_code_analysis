def A_Ex8(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(fileName, encoding="UTF-8")
    elem=f.read().split("\n")
    cont=0
    ris=[0,0]
    for i in range(0, len(elem)):
        for z in range(0,len(elem[i])):
            if ord(elem[i][z])>=65 or ord(elem[i][z])<=90:
                cont+=1
        if ris[1]<cont:
            ris[0]=i
            ris[1]=cont
        else:
            if ris[1]==cont:
                if ris[0]<i:
                    ris[0]=i
    return ris[0]+1
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
