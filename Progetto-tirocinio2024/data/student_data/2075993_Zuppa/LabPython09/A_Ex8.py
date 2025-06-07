def A_Ex8(fileName):
    fin=open(fileName,encoding='UTF-8')
    st=fin.read()
    fin.close()
    l=st.split('\n')
    M=0
    for k in range(len(l)):
        c=0
        for i in range(len(l[k])):
            if l[k][i].isupper():
                c+=1
        if M<=c:
            M=c
            rM=k
    return rM+1
 
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
