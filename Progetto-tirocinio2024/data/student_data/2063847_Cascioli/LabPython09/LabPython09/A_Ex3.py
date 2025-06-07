def A_Ex3(fileName):
    f=open(fileName, encoding="UTF-8")
    insieme=set()
    l=[]
    for i in f:
        i=i.strip().split(",")
        if(i[1]=="Voto"):
            continue
        i[1]=int(i[1])
        if(i[1]>=29 ):
            l.append(i[2])
    for j in range(len(l)):
        if(l.count(l[j])>=2):
            insieme.add(l[j])    
    return(insieme)

"""un altro for che conta sulle materie inserite sulla lista"""

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
