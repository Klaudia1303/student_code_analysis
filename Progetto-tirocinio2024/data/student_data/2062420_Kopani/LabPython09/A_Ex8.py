def A_Ex8(fileName):
    f=open(fileName,encoding="UTF-8")
    l=f.readlines()
    L=[]
    for i in range(len(l)):
        s=l[i]
        s1=s.replace('\n','')
        L.append(s1)
    f.close()
    LM=0
    riga=0
    for j in range(len(L)):
        Maiuscole=0
        for k in L[j]:
            if k.isupper():
                Maiuscole+=1
        if Maiuscole>=LM:
            LM=Maiuscole
            riga=j+1
    return(riga)
 
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
