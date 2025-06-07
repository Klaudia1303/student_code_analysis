def A_Ex8(fileName):

    f=open(fileName, encoding="UTF-8")
    ls=[]
    s=0
    p=0
    for i in f:
        i=i.strip().split(" ")
        ls.append(i)
    for j in range(len(ls)):
        for z in range(len(ls[j])):
            for c in range(len(ls[j][z])):
                if ls[j][z][c].isupper==True:
                    s=s+1
        if s>=p:
            p=s
            h=j+1
        s=0
    f.close()
    return h
 
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
