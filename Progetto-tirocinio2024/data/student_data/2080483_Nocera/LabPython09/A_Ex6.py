
def A_Ex6(filename):
    strn=[]
    totale=0
    i=1
    fin=open(filename,encoding="UTF-8")
    f1=fin.readline()
    anni=f1.strip().split(",")
    
    
    for riga in fin:
        r=riga.strip().split(",")
        strn.append(r)
        
    while i<len(anni):
        somma=0
        
        for elem in strn:
            somma=int(elem[i])+somma
        if somma>=totale:
            totale=somma
            anno=int(anni[i])
        i+=1
    fin.close()
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
