def A_Ex5(filename,oggetto):
    f=open(filename, encoding="UTF-8")
    l=[]
    for elem in f:
        elem=elem.strip().split(",")
        l.append(elem)
    f.close()
    l_anno = l[0]
    for i in range (len(l)):
        lista = l[i]
        if oggetto in lista :
            break
    cremax = 0
    for j in range(1, len(lista)-1):
        crescita = 0
        crescita = int(lista[j+1]) - int(lista[j])
        print(crescita)
        if crescita > cremax :
            cremax = crescita
            anno = l_anno[j+1]
        elif crescita == cremax :
            anno = l_anno[j+1]
        elif crescita < 0 and j == len(lista)-2 and cremax == 0:
            anno = l_anno[1]
    anno = int(anno)
    return(anno)


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
