def A_Ex3(fileName):
    f=open(fileName,encoding="UTF-8")
    
    l=[]
    i=set() #insieme delle materie
    sv=set() #insieme da restituire
    f.readline() #salta la prima riga perchè non ci sono dati, solo testo!!

    for line in f: #creo una lista fatta da liste (una lista per riga)
        s=line.strip().split(',')
        l.append(s)
    f.close()

    for e in l: #creo l'insieme delle materie
        i.add(e[2])

    for el in i: #per ogni materia
        k=0
        for elem in l: #per ogni elemento della lista 
            if elem[2]==el and int(elem[1])>28: #per ogni 29+ 
                k+=1
        if k>1: #se l'hanno preso 2+ persone lo aggiungo al risultato
            sv.add(el)
    
    return sv

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
