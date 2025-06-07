def A_Ex8(fileName):
    f=open(fileName,'r',encoding='UTF-8')
    iRiga=0
    contacharMax=0
    #indiceRiga=0
    for riga in f:     
        iRiga+=1
        contachar=0
        for char  in riga:     
            if char.isupper():
                contachar+=1
        if contacharMax<=contachar: 
             contacharMax=contachar
             indiceRiga=iRiga
    return indiceRiga
            
                
    
 
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
