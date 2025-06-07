def A_Ex8(fileName):
    fin=open(fileName,encoding='UTF-8')
    c='c'
    k=True
    maiu=0
    ris=0
    i=1
    iDef=1
    while k:
        c=fin.read(1)
        if c=='\n' or c=='':
            if maiu>=ris:
                iDef=i
                ris=maiu
            maiu=0
            i+=1
        if c.isupper():
            maiu+=1
        elif c=='':
            k=False
    return iDef
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
