def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    #Scrivere una funzione che prende in ingresso una stringa fileName che denota il nome di un file
    #csv nel formato di sopra e calcola in quale anno (numero intero) le vendite complessive sono state massime. Se ci
    #sono 2 anni con le stesse vendite, si prenda l’anno più grande. Ad esempio, se il file è quello di sopra allora deve
    #restituire 2010, anno in cui ci sono stati venduti in tutto 51 oggetti
    
    file=open(filename,"r",encoding="UTF-8")
    riga1=file.readline()
    riga1=riga1.strip().split(",")
    #lettura=file.read()
    file.close()

    tot=[]
    for i in range(1,len(riga1)):
        l=[]
        with open(filename,encoding="UTF-8") as file:
            for righe in file:
                righe=righe.strip().split(",")
                l.append(int(righe[i]))
            somma=sum(l)
            #print("somma vendite: ",somma," anno: ",riga1[i])
            tot.append(somma)
    #print(tot)
    for x in range(len(tot)):
        for h in range(len(tot)):
            if tot[x]==tot[h] and x!=h:
                if int(riga1[x+1])>int(riga1[h+1]):
                    return int(riga1[x+1])
        if tot[x]==max(tot):
            indice=x
            break
    return int(riga1[indice+1])

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
