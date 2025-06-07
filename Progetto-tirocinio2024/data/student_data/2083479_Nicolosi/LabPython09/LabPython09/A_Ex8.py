def A_Ex8(fileName):
    f=open(fileName,encoding='UTF-8')
    i=1
    massimo=0
    numero_riga=0
    for riga in f:
        lista=riga.split()
        conta_maiuscole=0
        for j in range(len(lista)):
            stringa=lista[j]
            for n in range(len(stringa)):
                if stringa[n].isupper()==True:
                    conta_maiuscole+=1
        if conta_maiuscole>=massimo:
            massimo=conta_maiuscole
            numero_riga=i
        i+=1
    return numero_riga
        
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
