def A_Ex8(fileName):
    f=open(fileName,encoding="UTF-8")
    testo=f.readlines()
    conto=0
    contomax=0
    rigamax=0
    for i in range(len(testo)):
        riga=testo[i]
        indice=i+1
        
        for lettera in riga:
            if lettera.islower()==True:
                conto+=1
                
            if conto>contomax:
                contomax=conto
                rigamax=indice
            if conto==contomax and indice>rigamax:
                rigamax=indice
    f.close()
                









    
    return rigamax
    
            






















    
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
