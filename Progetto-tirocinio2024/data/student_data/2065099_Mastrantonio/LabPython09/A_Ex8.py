def A_Ex8(fileName):
    f = open (fileName, encoding = "UTF-8")
    riga = 0
    massimo = 0
    for elem in f :
        c = 0
        riga = riga +1
        for i in range(len(elem)):
            if ord(elem[i]) > 64 and ord(elem[i])<91:
                c = c +1
        if c > massimo:
            massimo = c
            risultato = riga
    f.close()
    return(riga)
 
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
