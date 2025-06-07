def A_Ex6(filename):
    f=open(filename,'r',encoding='UTF-8')
    a=f.readline().strip().split(',') #prima riga, presa perchè fuori dal for
    M=0
    l=[]
    pos=1
    for line in f:
        s=line.strip().split(',')
        l.append(s)   
    for i in range(1,len(a)): #prendi l'anno dalla prima riga, so le posizioni degli anni
        somma=0
        for e in l: #prendi ciascuna riga dalla lista
            somma+=int(e[i]) #sommo tutti i numeri nella riga nella posizione dell'anno che sto considerando
        if somma>=M: #confronto le somme di ciascun anno 
            M=somma #conservo quella maggiore 
            pos=i #conservo la posizione dell'anno con somma maggiore
    f.close()
    res=int(a[pos]) #trovo l'anno nella prima riga, con somma maggiore
    return res
 
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
