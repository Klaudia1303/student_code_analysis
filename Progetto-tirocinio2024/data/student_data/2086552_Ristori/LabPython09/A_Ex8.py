def A_Ex8(fileName):
    fin=open(fileName,"r",encoding="UTF-8")
    lista=fin.readlines()
    conteggioMax=0
    for i in range(len(lista)):
        conteggio=0
        for j in range(len(lista[i])):
            if lista[i][j].isupper():
                conteggio+=1
        if conteggio>=conteggioMax:
            conteggioMax=conteggio
            indiceMax=i+1
    return int(indiceMax)
        
        








    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
