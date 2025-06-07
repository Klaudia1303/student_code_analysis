def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    file = open(filename,'r',encoding='UTF-8')
    incremento = 1
    anno = 1
    anni = file.readline().strip().split(',')
    #print(anni)
    somma = 0
    for i in range(1,len(anni)):
        sommaAct = 0
        #print(str(i) + ' index')
        
        file = open(filename,'r',encoding='UTF-8')
        file.readline()
        for riga in file:
            val = riga.strip().split(',')
            sommaAct +=int(val[i])
            #print( 'somma:' + val[i] + ' in posizione : ' + str(i))
        if(sommaAct > somma):
            somma = sommaAct
            anno = int(anni[i])
            sommaAct = 0
        elif(sommaAct == somma):
            if(int(anni[i]) > anno):
                somma = sommaAct
                anno = int(anni[i])
                sommaAct = 0
        file.close()
        
    return anno

    
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
