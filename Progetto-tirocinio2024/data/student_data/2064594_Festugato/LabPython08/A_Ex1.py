def A_Ex1(l):
    M = 0
    volte = 0
    caratteri = set()

    for s in l:
        for c in s:
            if c.islower():
                caratteri.add(c)#isolo i caratteri delle stringhe
    #print(caratteri)
                

    for i in caratteri: #per ogni carattere
        for s in l: #guardo su ciascuna stringa
            if s.count(i) > 0:
                volte += 1 #conta le stringhe in cui è presente il carattere
                
               # print(i,volte,s)

        if volte > M:
            M = volte
            carattereMax = i
            #print(M,carattereMax)
        elif volte == M and i > carattereMax:
            carattereMax = i

        volte = 0 #riazzero il conto per ogni carattere
            
            
    return carattereMax
                
    
    

    














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
