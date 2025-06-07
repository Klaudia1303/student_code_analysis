def A_Ex1(l):
    contamax = 0
    chr_finale = 'a'
    for i in range(len(l)):
        parola = l[i]
        for j in range (len(parola)):
            lettera = parola[j]
            conta = 0
            for k in range (len(l)):
                if lettera in l[k] and parola[j].islower():
                    conta = conta + 1
            if conta > contamax :
                contamax = conta
                chr_finale = lettera
            elif conta == contamax :
                if lettera > chr_finale :
                    contamax = conta
                    chr_finale = lettera
    return (chr_finale)

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
