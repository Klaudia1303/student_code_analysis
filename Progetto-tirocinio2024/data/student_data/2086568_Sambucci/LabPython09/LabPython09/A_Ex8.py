def A_Ex8(fileName):
    fin=open(fileName,encoding="UTF-8")
    f=fin.readlines()
    fin.close()
    contamax=0
    indmax=0
    for i in range(len(f)):
        conta=0
        for c in f[i]:
            if c.isalpha() and c.isupper():
                conta+=1
        if conta>contamax:
            contamax=conta
            indmax=i
        elif conta==contamax:
            if i>indmax:
                contamax=conta
                indmax=i
                
    return indmax+1
 
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
