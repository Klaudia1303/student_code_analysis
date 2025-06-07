def A_Ex3(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    #Scrivere una funzione che prende in ingresso una stringa fileName, nome di un file csv che ha
    #lo stesso formato del file descritto nell’esercizio precedente (A_Ex2), e restituisce un insieme contenente tutte e sole
    #le Materie per cui ci sono almeno due studenti che hanno preso almeno 29 (potete assumere che nel file non ci
    #siano mai due righe uguali, aventi stessa matricola e stessa materia – in altri termini, il file contiene un solo voto per
    #un certo studente ed una certa materia)

    file=open(fileName,"r",encoding="UTF-8")
    t=file.readline()
    insieme=set()
    l=[]
    for elem in file:
        elem=elem.strip().split(",")  #lista che contiente le varie sezioni della riga
        if int(elem[1])>=29:
            l.append(elem[2])
        if l.count(elem[2])>=2:
            insieme.add(elem[2])
    file.close()
    return insieme
       
    
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
