def A_Ex1(l):
    a=0
    risultato=""
    lunghezza=0
    conta=0
    for i in l:
        for k in i:
            while lunghezza<len(l):
                if k in l[lunghezza]:
                    conta+=1
                lunghezza+=1
            if k.isupper()or k.isdecimal():
                conta=-1
            if conta>a:
                a=conta
                risultato=k
            if conta==a and ord(k)>ord(risultato):
                a=conta
                risultato=k
            conta=0
            lunghezza=0
    return(risultato)
            
            
        

                

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
