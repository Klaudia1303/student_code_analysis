def A_Ex2(fileName):
    file=open(fileName,encoding='UTF-8')
    txt=file.read().split('\n')
    resultList=[]
    for elem in txt:
        subList=elem.split(',')
        if subList[0]=='':
            break
        if subList[1].isalpha()==False and int(subList[1])>=18:
            values=(subList[0],subList[2])
            resultList.append(values)
    file.close()
    return resultList


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