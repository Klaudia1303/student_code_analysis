def A_Ex5(filename,oggetto):
    fin=open(filename,encoding='UTF-8')
    ris=0
    anno=0
    for riga in fin:
        riga=riga.strip().split(',')
        if riga[0]==oggetto:
            for i in range(len(riga)):
                if i==0:
                    continue
                elif i==len(riga)-1:
                    continue
                else:
                    c=int(riga[i+1])-int(riga[i])
                    if c>=ris:
                        anno=i
                        ris=c
    fin=open(filename,'r',encoding='UTF-8')
    s=fin.readline()
    s=s.strip().split(',')
    for i in range(len(s)):
        k=(s[i])
        if i==anno+1:
            break
    return int(k)
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
