def A_Ex8(fileName):
    f=open(fileName,'r',encoding='UTF-8')
    riga=0
    rigamax=0
    righe=f.readlines()
    for elem in range(len(righe)):
        conta=0
        for parole in range(len(righe[elem])):
            c=righe[elem][parole]
            if c.upper() and c.isalpha():
                conta+=1
            if conta>=rigamax:
                massimo=conta
                riga=elem+1
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
