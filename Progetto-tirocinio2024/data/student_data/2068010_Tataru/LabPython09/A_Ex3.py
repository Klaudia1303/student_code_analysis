def A_Ex3(fileName):
    f=open(fileName,encoding="UTF-8")
    s=f.readlines()
    for i in range(0,len(s)):
        s[i]=s[i].replace("\n","")
        for elem in '.,;:!?<>"-«»()\'':
            s[i]=s[i].replace(elem," ")
    lm1=[]
    r=[]
    for i in range(1,len(s)):
        l=s[i].split()
        while (len(l)>3):
            l[2]+=" "+l[3]
            l.remove(l[3])
        if (int(l[1])>28):
            if(l[2] in lm1):
                r.append(l[2])
            else:
                lm1.append(l[2])
                

    
    return set(r)

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
