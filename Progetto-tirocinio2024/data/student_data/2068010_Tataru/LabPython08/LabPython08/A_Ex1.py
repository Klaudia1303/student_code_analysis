def A_Ex1(l):
    lc=[]
    for i in range (0,26):
        lc.append(0)
    for i in l:
        i="".join(sorted(i))
        while (len(i)>0):
            if(ord(i[0])-97<0):
                i=i[1:len(i)]
                continue
            lc[ord(i[0])-97]+=1
            t=i[0]
            while (i.count(t)>0):
                i=i[1:len(i)]
    for i in range(25,-1,-1):
        if (lc[i]==max(lc)):
            return(chr(97+i))

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
