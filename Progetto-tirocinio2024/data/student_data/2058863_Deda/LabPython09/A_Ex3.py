def A_Ex3(fileName):
    f=open(fileName,'r',encoding="UTF-8")
    t=f.readlines()
    o=[]
    for i in range(len(t)):
        y=''
        q=t[i].split(',')
        w=q[2]
        for j in range(len(w)):
            if w[j]!='\n':
                y+=w[j]
        o.append(q[0])
        o.append(q[1])
        o.append(y)
    v=set()
    for k in range(3,len(o),3):
        b=int(o[k+1])
        c=o[k+2]
        if b>=29 and o.count(c)>=2:
            v.add(c)
    return v

    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
