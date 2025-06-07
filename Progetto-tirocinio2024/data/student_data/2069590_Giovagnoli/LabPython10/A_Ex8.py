def A_Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    #La funzione deve leggere il file e costruire un dizionario avente come chiavi i nomi di tutte le persone che
    #compaiono nel file, e per valore associato a ciascuna chiave k la lista ordinata in ordine lessicografico
    #crescente degli amici di k (rimasti al termine della lista). Ogni volta in cui 2 persone diventano amiche
    #dovete aggiungere il nome di ciascuno dei due alla lista degli amici dell’altro, se non era già presente (non
    #ci devono essere duplicati nella lista). Se due persone diventano nemiche dovete eliminare il nome di
    #ciascuno dei due dalla lista degli amici dell’altro (se c’era, altrimenti non dovete fare niente).

    f=open(file,encoding="UTF-8")
    f.readline()
    d={}
    l=[]
    for riga in f:  
        riga=riga.strip().split(",")   #lista(riga)
        if riga[2]=='amici':
            if riga[0] not in d:
                d[riga[0]]=[riga[1]]
            elif riga[1] not in d[riga[0]]:
                d[riga[0]].append(riga[1])
            
            if riga[1] not in d:
                d[riga[1]]=[riga[0]]
            elif riga[0] not in d[riga[1]]:
                d[riga[1]].append(riga[0])

        else:
            if riga[0] in d and riga[1] in d[riga[0]]:
                d[riga[0]].remove(riga[1])
            if riga[1] in d and riga[0] in d[riga[1]]:
                d[riga[1]].remove(riga[0])

    chiavi=d.keys()
    for x in chiavi:
        d[x].sort()
    return d



                



    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["amici1.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici2.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria'], 'Maria': ['Anna'], 'Paola': [], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici3.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici4.csv"] , {'Marco': ['Giorgio', 'Paolo'], 'Giorgio': ['Marco'], 'Paolo': ['Marco'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna']})
    counter_test_positivi += tester_fun(A_Ex8, ["amici5.csv"] , {'Marco': [], 'Giorgio': [], 'Paola': [], 'Anna': []})

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
