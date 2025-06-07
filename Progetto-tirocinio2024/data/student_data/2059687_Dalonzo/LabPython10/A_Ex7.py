def A_Ex7(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    partite = open(file,'r',encoding='UTF-8')
    partite.readline()
    squadre = []
    rate = {}
    for riga in partite:
        values = riga.strip().split(',')
        if(values[0] not in squadre):
            squadre.append(values[0])
        if(values[1] not in squadre):
            squadre.append(values[1])

    partite.close()
    partite = open(file,'r',encoding='UTF-8')
    partite.readline()
    for riga in partite:
        values = riga.strip().split(',')
        if(int(values[2]) > int(values[3])):
           if(values[0] not in rate):
               rate[values[0]] = 3
           else:
                rate[values[0]] = rate[values[0]] + 3
           if(values[1] not in rate):
               rate[values[1]] = 0
           
                                      
        elif(int(values[2]) == int(values[3])):
            if(values[0] not in rate):
               rate[values[0]] = 1
            else:
                rate[values[0]] = rate[values[0]] + 1

            if(values[1] not in rate):
               rate[values[1]] = 1
            else:
                rate[values[1]] = rate[values[1]] + 1
                                      
        elif(int(values[2]) < int(values[3])):
            if(values[1] not in rate):
               rate[values[1]] = 3
            else:
                rate[values[1]] = rate[values[1]] + 3
            if(values[0] not in rate):
               rate[values[0]] = 0
               
        
    partite.close()       
    return rate
            
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, ["partite1.csv"] , {'Chelsea': 3, 'Everton': 3, 'Arsenal': 4, 'Tottenham': 1})
    counter_test_positivi += tester_fun(A_Ex7, ["partite2.csv"] , {'Chelsea': 4, 'Everton': 6, 'Arsenal': 4, 'Tottenham': 2})
    counter_test_positivi += tester_fun(A_Ex7, ["partite3.csv"] , {'Bayern': 4, 'Schalke': 3, 'Amburgo': 4, 'Werder': 1, 'Colonia': 4, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite4.csv"] , {'Bayern': 8, 'Schalke': 6, 'Amburgo': 8, 'Werder': 2, 'Colonia': 8, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite5.csv"] , {'Bayern': 5, 'Schalke': 6, 'Amburgo': 5, 'Werder': 5, 'Colonia': 5, 'Stoccarda': 6})

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
