def A_Ex1(l):
    count0=0
    car="a"
    count1=0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j].islower():
                for k in range(len(l)):
                    if l[i][j] in l[k]:
                        count1+=1
                if count1>count0:
                    count0=count1
                    count1=0
                    car=l[i][j]
                elif count1==count0:
                    if l[i][j]>car:
                        car=l[i][j]
                        count1=0
                    else:
                        count1=0
                else:
                    count1=0
    return car
    
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
