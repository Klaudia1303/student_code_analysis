def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    lista=[]
    somma=0
    mass=1
    pos=1

    f=open(filename, encoding='UTF-8')
    primariga=f.readline().strip().split(',')
    for riga in f:
        riga=riga.strip().split(',')
        lista.append(riga)

        for i in range (1, len(riga)):
            f2=open(filename, encoding='UTF-8')
            
            for riga2 in f2:
                riga2=riga2.strip().split(',')
                if riga2[0]!='Anno':
                    somma=somma+int(riga2[i])

            f2.close()
           
            if somma>=mass:
                mass=somma
                pos=i
            somma=0
    return (int(primariga[pos]))
            
                
        
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
