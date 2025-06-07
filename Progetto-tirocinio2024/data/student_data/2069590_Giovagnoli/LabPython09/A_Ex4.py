def A_Ex4(filename,anno):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    #Scrivere una funzione che prende in ingresso una stringa fileName che denota il nome di
    #un file csv che contiene le informazioni sul numero e tipo di oggetti venduti in anni consecutivi da un negozio, ed un
    #intero anno che denota un anno (che potete assumere siano tra quelli presenti nel file) e restituisce il nome
    #dell’oggetto più venduto in quell’anno. Il file è nel seguente formato (come esempio, ma il numero di anni potrebbe
    #variare):

    file=open(filename,"r",encoding="UTF-8")
    l=[]
    l1=[]
    indice=0
    indice_finale=0
    riga=file.readline()
    riga=riga.strip().split(",")
    for i in range(1,len(riga)):
        if int(riga[i])==anno:
            indice=i
            break

    for righe in file:
        righe=righe.strip().split(",")
        voto=righe[indice]
        l.append(int(voto))
        #print("l:",l)
        l1.append(righe[0])
        #print("l1:",l1)

    mass=max(l)
    for y in range(len(l)):
        if mass==l[y]:
            indice_finale=y
            break

    file.close()
    return l1[indice_finale]            
    

            
        
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
