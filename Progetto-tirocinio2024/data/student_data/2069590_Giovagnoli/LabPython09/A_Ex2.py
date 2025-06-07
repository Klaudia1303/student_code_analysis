def A_Ex2(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    #Scrivere una funzione che prende ingresso una stringa fileName, nome di un file csv, contenente
    #le informazioni sugli esami superati dagli studenti (nel formato Matricola,Voto,Materia), e restituisce una
    #lista contenente tutte e sole le coppie (Matricola, Materia) per gli esami superati, tali cioè che lo studente con
    #quella matricola abbia preso un voto maggiore o uguale a 18. Notare che una coppia è semplicemente una tupla di
    #lunghezza due. Le coppie devono comparire nella lista nello stesso ordine in cui le informazioni si trovano nel file.

    file=open(fileName,encoding="UTF-8")
    t=file.readline()
    lista=[]
    for riga in file:
        l=[]
        riga=riga.strip().split(",")
        for elem in range(0,len(riga),2):
            if int(riga[1])>=18:
                l.append(riga[elem])
        if len(l)>0:
            tupla=tuple(l)
            lista.append(tupla)
    file.close()
    return lista
            
        
        
    
        
            
        
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex2, ["esami1.csv"], [('1345','Fisica'),('1346','Analisi'),('1896','Geometria'),('1753','Fisica')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami2.csv"], [('1346','Analisi')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami3.csv"], [('1347', 'Analisi'), ('1348', 'Analisi'), ('1347', 'Ricerca Operativa'), ('1349', 'Ricerca Operativa')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami4.csv"], [('1100', 'Basi di Dati'), ('1012', 'Basi di Dati'), ('1021', 'Analisi')])
    counter_test_positivi += tester_fun(A_Ex2, ["esami5.csv"], [('1345','Fisica'),('1987','Fondamenti'),('1346','Analisi'),('1896','Geometria')])

    print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
