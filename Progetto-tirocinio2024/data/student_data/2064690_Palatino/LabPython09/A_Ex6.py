def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    with open(filename,'r',encoding="UTF-8") as f:
        s=f.readline().strip().split(',')
        (_,anni)=(s[0],s[1:])
        massimovend=0
        massimovendanno=0
        righe=f.readlines()
        for i in range(len(anni)):
            venditeannocorrente=0
            for riga in righe:
                riga=riga.strip().split(',')
                venditeannocorrente+=int(riga[i+1])

            if venditeannocorrente>massimovend:
                massimovend=venditeannocorrente
                massimovendanno=int(anni[i])
            elif venditeannocorrente==massimovend:
                massimovendanno=max(massimovendanno, int(anni[i]))
        return massimovendanno
 
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
