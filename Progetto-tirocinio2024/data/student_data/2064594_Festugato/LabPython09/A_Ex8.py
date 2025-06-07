def A_Ex8(fileName):
    file = open(fileName,'r',encoding= 'UTF-8')

    i = 1
    M = 0
    n = 0

    for righe in file:
        for c in righe:
            if c.isupper() == True:
                n += 1
        if n >= M:
            M = n
            riga = i
        i += 1

    return riga
            
        
    
   
 

































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
