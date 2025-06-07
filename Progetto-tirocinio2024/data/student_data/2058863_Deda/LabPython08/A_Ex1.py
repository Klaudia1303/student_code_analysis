def A_Ex1(l):
    massimo=0
    d=''
    for i in range(len(l)):
        a=str(l[i])
        for j in range(len(a)):
            conta=0
            b=a[j]
            for k in range(len(l)):
                c=l[k]
                if (b in c) and b.islower():
                    conta+=1
                if conta>massimo:
                    massimo=conta
                    d=b
                elif conta==massimo:
                    if b>d:
                        d=b
    return d
                
            
        
    
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
