def A_Ex1(l):
    massimo=0
    carattere_massimo='A'
    for i in range(len(l)):
        stringa=l[i]
        for carattere in range(len(stringa)):
            c=stringa[carattere]
            conto=0
            for x in range(len(l)):
                if c in l[x] and x!=i and stringa[carattere].islower():
                    conto+=1
            if conto>massimo:
                massimo=conto
                carattere_massimo=c
            elif massimo==conto:
                if c>carattere_massimo:
                    carattere_massimo=c
    return carattere_massimo
                
  
                

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
