def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    fin=open(filename,encoding="UTF-8")
    s_tot=[]
    for elem in fin:
        elem=elem.strip().split(',')
        s_tot.append(elem)
    fin.close()

    somma=0
    max_somma=0

    for j in range(1,len(s_tot[0])):

        for i in range(1,len(s_tot)):
        
            somma+=int(s_tot[i][j])
            
        if somma>=max_somma:
            max_somma=somma
            anno=int(s_tot[0][j])
        somma=0
     #i colonna j riga
    return(anno)
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
