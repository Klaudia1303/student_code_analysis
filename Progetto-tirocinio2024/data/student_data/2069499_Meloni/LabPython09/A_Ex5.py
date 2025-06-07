def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    fin=open(filename,encoding="UTF-8")
    s_tot=[]
    crescita_max=0
    for elem in fin:
        elem=elem.strip().split(',')
        s_tot.append(elem)
    fin.close()

    oggetti=[s_tot[i][0] for i in range(1,len(s_tot))]   
    colonna=(oggetti.index(oggetto))+1

    max_anno=int(s_tot[0][1])
    valori=[s_tot[colonna][i] for i in range(1,len(s_tot[colonna]))]

    for i in range (len(valori)-1):
        if int(valori[i+1])>=int(valori[i]):
            crescita=int(valori[i+1])-int(valori[i])
            if crescita>=crescita_max:
                crescita_max=crescita
                max_anno=int(s_tot[0][i+2])
                
    return(max_anno)
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
