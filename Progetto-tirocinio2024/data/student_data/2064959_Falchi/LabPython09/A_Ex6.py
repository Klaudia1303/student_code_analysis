def A_Ex6(fileName):
    
    numeroAnni = 0
    anni = list()

    year = None

    with open(fileName, "r", encoding = "UTF-8") as file:
        titoli = file.readline().strip().split(",")

        for i in range(1, len(titoli)):
            numeroAnni += 1
            anni.append(titoli[i])

        print(numeroAnni, anni)

        somme = [0 for i in range(numeroAnni)]
        print(somme)

        for rigaGrezza in file:
            riga = rigaGrezza.strip().split(",")
            
            for i in range(1, len(riga)):
                somme[i-1] += int(riga[i])

        print(somme)
        anni.reverse()
        somme.reverse()

        year = int(anni[somme.index(max(somme))])

    return year
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
