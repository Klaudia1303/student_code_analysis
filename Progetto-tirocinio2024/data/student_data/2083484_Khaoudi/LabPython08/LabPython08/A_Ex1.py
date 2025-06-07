def A_Ex1(l):
    """MODIFICARE IL CO NTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    charGlobal=""
    countCharGlobal=0
    for elemento in l :
        for i in range(len(elemento)):
            char=elemento[i]
            countChar=0
            countTot=0
            for k in l:
                if char.lower() == char and not char.isnumeric():
                    if char in k:
                        countChar +=1
            if countChar > countCharGlobal:
                charGlobal=char
                countCharGlobal=countChar
            if countChar == countCharGlobal:
                if charGlobal < char:
                    charGlobal=char
            print(charGlobal)
    return charGlobal

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex1, [["casa", "senape", "ketchup", "pasta"]] , "s")
    counter_test_positivi += tester_fun(A_Ex1, [["a", "b", "b", "a", "a", "a", "a"]] , "a")
    counter_test_positivi += tester_fun(A_Ex1, [["1fI", "1FI", "1FI", "1FI","1FI" ]] , "f")
    counter_test_positivi += tester_fun(A_Ex1, [["conte", "dpcm"]] , "c")
    counter_test_positivi += tester_fun(A_Ex1, [["Zlatan", "Ibraimovich", "Cristiano", "Ronaldo", "Francesco", "Totti"]] , "o")


    print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
