def A_Ex6(filename):
    a=open(filename, encoding="UTF-8")
    sv=[]
    y=-1
    t=0
    anno=0
    for elem in a:
        elem=elem.strip().split(",")
        sv.append(elem)
    y=0
    t=0
    for i in range(1,len(sv[0])):
                   for j in range(1,len(sv)):
                       t += int(sv[j][i])
                       if t>y:
                           y=int(t)
                           anno=int(sv[0][i])
    return anno
                       
    
    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
