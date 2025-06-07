def A_Ex6(filename):
    listItems=[]
    file=open(filename)
    line=file.readline().strip().split(',')
    while line!=['']:
        listItems.append(line)
        line=file.readline().strip().split(',')
    print(listItems)
    top=0
    for counter in range(1,(len(listItems[0]))):
        current=0
        for counter2 in range(1,(len(listItems)-1)):
            current+=int(listItems[counter2][counter])
        if current>=top:
            topYear=listItems[0][counter]
            top=current
    file.close()
    return int(topYear)
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
