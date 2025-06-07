def A_Ex6(filename):
    f=open(filename,encoding="UTF-8")
    t=f.readlines()
    testo=[]
    conto=0
    contomax=0
    datamax=0
    

    for i in t:
        testo.append(i.strip().split(','))

    riga1=testo[1]
    date=testo[0]

    for x in range(1,len(riga1)):
        posizione=riga1[x]
        conto=0
        for y in range(1,len(testo)):
            riga=testo[y]
            numero=int(riga[x])
            data_corr=int(date[x])
            conto+=numero
        if conto>=contomax:
            contomax=conto
            datamax=int(date[x])
        
        
            

    f.close()
            
        
    return datamax


















    
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
