def A_Ex1(l):

    Lettere = [chr(i) for i in range(ord('a'), ord('z')+1)]
    Valori = [0 for i in range(len(Lettere))]

    #print(Lettere, Valori)
    
    for i in range(len(l)):
        for k in range(len(Lettere)):
            if Lettere[k] in l[i]:
                Valori[k] += 1
                #print(Lettere[k])
                #print(Valori[k])

    print()

    print(Lettere, Valori)
    
    Valori.reverse()
    Lettere.reverse()
    
    return Lettere[Valori.index(max(Valori))]
                    

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
