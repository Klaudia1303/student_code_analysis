def A_Ex1(fileName):
    result = 0
    with open(fileName) as f:
        t = f.read()
        non_alfa = []
        for c in t:
            if c not in non_alfa and not c.isalpha():
                non_alfa.append(c)
        for c in non_alfa:
            t = t.replace(c, ' ')
        parole = t.split()
        for c in parole:
            result += len(c)
    return result
    








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
