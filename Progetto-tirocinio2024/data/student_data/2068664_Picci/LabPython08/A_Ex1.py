def A_Ex1(l):
    cont=0
    lettera=''
    cont2=0
    for i in range(0,len(l)):
        for c in range(0,len(l[i])):
            cont2=0
            for j in range(0,len(l)):
                if l[i][c].islower() and l[i][c] in l[j]:
                    cont2+=1
                    if cont2>cont:
                        cont=cont2
                        lettera=l[i][c]
                    elif cont2==cont:
                        if ord(l[i][c])>ord(lettera):
                            lettera=l[i][c]
    return lettera
    
    

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
