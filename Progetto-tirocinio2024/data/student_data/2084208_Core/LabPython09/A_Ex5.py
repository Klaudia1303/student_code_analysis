def A_Ex5(filename,oggetto):
    f=open(filename)
    l=[]
    riga=f.readline()
    anni=riga.strip().split(',')
    riga=f.readline()
    oggett0=riga.strip().split(',')
    while len(riga)>0:
        if oggett0[0]==oggetto:
            for i in oggett0:
                l.append(i)
        riga=f.readline()
        oggett0=riga.strip().split(',')
    precedente=0
    numero=0
    print (l)
    for j in range(1,len(l)-1):
        if (int(l[j+1])-int(l[j]))>precedente:
            precedente=int(l[j+1])-int(l[j])
            numero=l[j+1]
        if (int(l[j+1])-int(l[j]))==precedente:
            numero=max(l[j+1],numero)
    if numero==0:
        precedente=(int(l[1])-0)
        numero=l[1]
        for z in range(2,len(l)-1):
            if int(l[z+1])-int(l[z])>precedente:
                precedente=int(l[z+1])-int(l[z])
                numero=l[z+1]
            elif int(l[z+1])-int(l[z])==precedente:
                numero=max(l[z+1],numero)
    indice_anno=l.index(numero)
    anno=anni[indice_anno]
    return int(anno)

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
