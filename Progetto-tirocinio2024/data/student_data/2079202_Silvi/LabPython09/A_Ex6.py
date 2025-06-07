def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(filename,encoding="UTF-8")
    anni=list(f.readline().strip().split(","))
    
    d={}
    for elem in f:
        if elem.split(",")[0]!="Anno":
            for i in range(1,len(anni)):
                if anni[i] in d:
                    d[anni[i]]+=int(elem.strip().split(",")[i])
                else:
                    d[anni[i]]=int(elem.strip().split(",")[i])
                           
    return int(max(d, key=d.get))
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
