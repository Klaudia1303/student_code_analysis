def A_Ex6(filename):
    fin=open(filename)
    L=[]
    somma=0
    max_vendite=0
    i=1
    best=''
    for riga in fin:
        riga=riga.strip().split(',')
        L.append(riga)    
    while i<len(L[0]):
        somma=0
        for j in range(1,len(L)):
            somma=somma+int(L[j][i])    
        if somma>=max_vendite:
            max_vendite=somma
            best=L[0][i]
        i=i+1
    fin.close()    
    return int(best)   
            
        
        
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
