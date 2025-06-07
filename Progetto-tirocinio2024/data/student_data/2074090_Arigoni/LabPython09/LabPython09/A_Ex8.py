def A_Ex8(fileName):
    f=open(fileName,encoding="utf-8")
    s=f.readlines()
    for i in range(len(s)):
        LettereM=0
        RG=0
        CR=0
        for e in range(len(s[i])):
            if ord(s[i][e])>64 and ord(s[i][e])<91:
                LettereM=LettereM+1
                if LettereM>RG:
                    RG=LettereM
                    CR=i+1
    return CR



















    
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
