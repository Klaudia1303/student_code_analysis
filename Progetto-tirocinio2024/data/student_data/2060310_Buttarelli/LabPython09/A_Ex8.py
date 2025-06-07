def A_Ex8(fileName):
    f = open(fileName, encoding = "UTF-8")
    l = []
    contatore = 0
    massimo = 0
    riga = 0
    for i in f:
        i = i.strip().split()
        l.append(i)
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j].strip
            for c in l[i][j]:
                if c.isupper():
                    contatore += 1
        if contatore >= massimo:
            massimo = contatore
            riga = int(l.index(l[i])) + 1
        contatore = 0

    f.close()
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
