def A_Ex5(filename,oggetto):
    file=open(filename,encoding='UTF-8')
    anni=file.readline()
    anni=anni.replace(',',' ').split()
    oggetti=file.readlines()
    maxcrescita=0
    for anno in range(len(anni[1:])):
        for elem in oggetti:
            elem=elem.strip().split(',')
            if elem[0]==oggetto:
                
                if elem[anno+1]>=elem[anno]:
                    crescita=int(elem[anno+1])-int(elem[anno])
                    if crescita>=maxcrescita:
                       maxcrescita=crescita
                       annocres=int(anni[anno+1])
    if maxcrescita==0:
        annocres=int(anni[1])
    return annocres
    

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
