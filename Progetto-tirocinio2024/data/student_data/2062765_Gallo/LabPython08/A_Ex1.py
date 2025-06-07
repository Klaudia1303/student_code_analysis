def A_Ex1(l):
    insieme=set()
    l2=[]
    
    for i in range(len(l)):
        x=set(l[i].lower())
        y=list(x)
        l2.append(y)
        x.clear()
    carattere=l2[0][0]
    c=0
    for j in range(len(l2)):
        for k in range(len(l2[j])):
            if l2.count(chr(l2[j][k]))>0:
                c=l2.count(l2[j][k])
                carattere=chr(l2[j][k])
            elif l2.count(l2[j][k])==c:
                if ord(l2[j][k])>ord(carattere):
                    carattere=chr(l2[j][k])
    return carattere
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
