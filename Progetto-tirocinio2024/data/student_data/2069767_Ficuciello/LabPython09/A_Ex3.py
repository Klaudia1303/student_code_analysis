def A_Ex3(fileName):
    f=open(fileName, encoding="UTF-8")
    l=set()
    sv=[]
    c=0
    for riga in f:
        riga=riga.strip().split(",")
        sv.append(riga)
    for elem in range(1,len(sv)):
        materie=[]
        if int(sv[elem][1])>=29 :
            c+=1
            materie.append(sv[elem][2])
            if int(c)>=2:
                l.add(sv[elem][2])
    f.close()
    return(l)
        
    

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
