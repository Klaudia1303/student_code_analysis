def A_Ex8(fileName):
    l=[]
    l1=[]
    cont=0
    f=open(fileName,encoding='UTF-8')
    for riga in f:
        l.append(riga)
    for i in range(len(l)):
        for j in range(len(l[i])):
            if 65<=ord(l[i][j])<=90:
                cont+=1
    l1.append(cont)
          
    x=max(l1)
    indice=l1.index(x)
    return indice
    
    






    
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
