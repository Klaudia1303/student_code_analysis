def A_Ex8(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(fileName,encoding='UTF-8')
    maiuscolemax=0
    indice=1
    indicemax=1
    for riga in f:
        riga=riga.strip().split()
        maiuscoleriga=0
        for i in range(len(riga)):
            for j in range(len(riga[i])):
                if ord(riga[i][j])>64 and ord(riga[i][j])<91:
                    maiuscoleriga+=1
        if maiuscoleriga>=maiuscolemax:
            maiuscolemax=maiuscoleriga
            indicemax=indice
        indice+=1
    return indicemax



 
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
