def A_Ex6(filename):
    file = open(filename,'r',encoding = 'UTF-8')

    anni = file.readline().strip().split(',')
   # print(anni,len(anni))

    file.close()

    i = 1
    somma = 0
    M = 0

    while i<len(anni):#itera sulle colonne

        file = open(filename,'r',encoding = 'UTF-8')

        anni = file.readline().strip().split(',')
        
        #print('i',i)
        for riga in file:
           riga = riga.strip().split(',')
           valori = int(riga[i]) #prende valore in colonna i di ogni riga
           somma += valori
           #print(somma)

        if somma > M:
           M = somma
           #print('M=',M)
           anno = anni[i]
        elif somma == M and anni[i] > anno:
           anno = anni[i]
        i += 1
        somma = 0
        file.close()

    return int(anno)

        
       

   
   

































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
