#Scrivere una funzione che prende ingresso una stringa fileName, nome di un file csv, contenente 
#le informazioni sugli esami superati dagli studenti (nel formato Matricola,Voto,Materia), e restituisce una 
#lista contenente tutte e sole le coppie (Matricola, Materia) per gli esami superati, tali cioè che lo studente con 
#quella matricola abbia preso un voto maggiore o uguale a 18. Notare che una coppia è semplicemente una tupla di 
#lunghezza due. Le coppie devono comparire nella lista nello stesso ordine in cui le informazioni si trovano nel file. 
#Ad esempio, se il file contiene
#Matricola,Voto,Materia
#1345,29,Fisica
#1987,17,Fondamenti
#1346,27,Analisi
#1896,30,Geometria
#1753,30,Fisica
#La funzione deve restituire 
#[('1345','Fisica'),('1346','Analisi'),('1896','Geometria'),('1753','Fisica')]
def A_Ex2(fileName):
    a=open(fileName,'r',encoding='UTF-8')
    casa=True
    stringa=''
    i=0
    u=''
    k=''
    risultato=[]
    while casa:
        stringa=a.readline()
        u=stringa.split(',')
        if len(stringa)==0:
            break
        if i>0:
            if int(u[1])>=18:
                k=u[2].replace('\n','')
                print(u[2])
                tupla=u[0],k
                risultato.append(tupla)
        i+=1
    return risultato
        
    
   
    
    
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
