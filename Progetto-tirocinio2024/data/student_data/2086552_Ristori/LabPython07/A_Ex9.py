def A_Ex9(l):
    lista=[]
    for i in range(len(l)):
        elem=l[i]
        massimo=0
        carMassimo=''
        for j in range(len(elem)):
            if elem.count(elem[j])>massimo:
                massimo=elem.count(elem[j])
                carMassimo=elem[j]
            if elem.count(elem[j])==massimo:
                if ord(elem[j])<ord(carMassimo):
                    massimo=elem.count(elem[j])
                    carMassimo=elem[j]
        lista.append(carMassimo)
    return lista
            
        










    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, [['amaca','amaranto','rosso']], ['a','a','o'])
    counter_test_positivi += tester_fun(A_Ex9, [['osso','assolato','alto']], ['o','a','a'])
    counter_test_positivi += tester_fun(A_Ex9, [['stringa','a','bbbbcccc','dado']], ['a','a','b','d'])
    counter_test_positivi += tester_fun(A_Ex9, [['fosso','dosso','rosso','fosso']], ['o', 'o', 'o', 'o'])
    counter_test_positivi += tester_fun(A_Ex9, [['ciao mamma','ciao ']], ['a', ' '])

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
