def A_Ex8(fileName):
    f=open(fileName, encoding='UTF-8')
    righe=f.readlines()
    max1=0
    ind=0
    for i in range(len(righe)):
        cont=0
        riga=righe[i]
        for j in range(len(riga)):
            if(riga[j].isupper()):
               cont+=1   
        if(cont>=max1):
            max1=cont
            ind=i+1
    f.close()
    return ind
               
 
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
