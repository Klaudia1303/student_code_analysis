def A_Ex1(l):
    appo=''
    occmax=0
    cmax='a'
    for i in range(len(l)):
        appo=l[i]
        for j in range(len(appo)):
            occ=0
            if appo[j]==appo[j].lower() and appo[j].isalpha()==True:
                occ+=1
                for k in range(i,len(l)):
                    appo2=l[k]
                    if appo2.find(appo[j])!=-1:
                        occ+=1
                if occ>occmax:
                    occmax=occ
                    cmax=appo[j]
                elif occ==occmax and appo[j]>cmax:
                    occmax=occ
                    cmax=appo[j]
    return cmax

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
