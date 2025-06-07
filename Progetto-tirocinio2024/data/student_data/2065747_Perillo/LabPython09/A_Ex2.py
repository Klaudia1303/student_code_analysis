def A_Ex2(fileName):
    a=open(fileName,"r",encoding="utf-8")
    casa=True
    stringa=""
    i=0
    u=""
    k=""
    risultato=[]
    while casa:
        stringa=a.readline()
        u=stringa.split(",")
        if len(stringa)==0:
            break
        if i>0:
            if int(u[1])>=18 :
                k=u[2].replace("\n","")
                print(u[2])
                tupla=u[0],k
                risultato.append(tupla)
        i+=1
    return(risultato)
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex2, ["esami1.csv"], [('1345','Fisica'),('1346','Analisi'),('1896','Geometria'),('1753','Fisica')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami2.csv"], [('1346','Analisi')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami3.csv"], [('1347', 'Analisi'), ('1348', 'Analisi'), ('1347', 'Ricerca Operativa'), ('1349', 'Ricerca Operativa')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami4.csv"], [('1100', 'Basi di Dati'), ('1012', 'Basi di Dati'), ('1021', 'Analisi')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami5.csv"], [('1345','Fisica'),('1987','Fondamenti'),('1346','Analisi'),('1896','Geometria')])

    print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
