def A_Ex1(fileName):
    str1=0
    f=open(fileName, 'r', encoding='UTF-8')
    s=f.read()
    f.close()
    for stringa in s:
        if stringa.isalpha()==True: #ciao
            str1+=1

    return str1

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
