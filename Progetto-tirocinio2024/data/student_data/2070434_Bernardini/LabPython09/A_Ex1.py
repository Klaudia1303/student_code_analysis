def A_Ex1(fileName):
    s=open(fileName, encoding="UTF-8")
    f=s.read()
    r=f.strip()
    z=0
    for i in range(0,252):
        d=chr(i)
        if d.isalpha():
            z=z+r.count(d)
    return z
            
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, ["Esempio1.txt"], 7)
    counter_test_positivi += tester_fun(A_Ex1, ["Esempio2.txt"], 53)
    counter_test_positivi += tester_fun(A_Ex1, ["Esempio3.txt"], 26)
    counter_test_positivi += tester_fun(A_Ex1, ["I_Malavoglia_50.txt"], 11808)
    counter_test_positivi += tester_fun(A_Ex1, ["I_Malavoglia.txt"], 382468)

    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
