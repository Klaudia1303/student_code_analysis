def A_Ex2(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    output=dict()
    f=open(file,encoding="UTF-8")
    a=f.readlines()
    f.close()
    for i in range (len(a)):
        b=a[i].strip().split(" ")
        for c in b:
            if c in output:
                output[c].add(i+1)
            else:
                output[c]={i+1}
    return output
         
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex2, ['testo1.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2}, 'al': {1}, 'lardo': {1}, 'che': {1}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3}})
    counter_test_positivi += tester_fun(A_Ex2, ['testo2.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'al': {1}, 'lardo': {1}, 'che': {1}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3, 4}})
    counter_test_positivi += tester_fun(A_Ex2, ['testo3.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3, 4}})
    counter_test_positivi += tester_fun(A_Ex2, ['testo4.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1}, 'zampone': {3}, 'zampina': {4}})
    counter_test_positivi += tester_fun(A_Ex2, ['testo5.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1}, 'zampone': {3, 6}, 'zampina': {4}, 'palla': {5}})

    print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
