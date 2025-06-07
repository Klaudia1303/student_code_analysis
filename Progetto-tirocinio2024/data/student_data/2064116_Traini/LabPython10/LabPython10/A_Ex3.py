#A_Ex3(fileName): Scrivere una funzione che prende ingresso una stringa fileName, nome di un file csv, 
#contenente le informazioni sugli esami superati dagli studenti (nel formato 
#Matricola,Voto,Materia), e restituisce un dizionario con chiave il nome dell’esame e valore la lista 
#ordinata delle matricole (rappresentate come interi) che hanno superato quell’esame, cioè hanno preso 
#almeno 18. Ad esempio, se il file contiene
#Matricola,Voto,Materia
#1345,29,Fisica
#1987,17,Fondamenti
#1346,27,Analisi
#1896,30,Geometria
#1753,30,Fisica
#La funzione deve restituire 
#{'Fisica': [1345,1753], 'Analisi': [1346], 'Geometria': [1896]}
def A_Ex3(fileName):
    f=open(fileName,'r',encoding='UTF-8')
    l=[]
    d={}
    for riga in f:
        l.append(riga.strip().split(','))
    for i in range(1,len(l)):
        if not l[i] [2] in d and int(l[i] [1])>17:
            d[l[i] [2]]=[]
        if int (l[i] [1])>17:
            d[l[i] [2]].append(int(l[i] [0]))
            d[l[i] [2]].sort()
    f.close()

    return d



                                   
                
                
                
        
        
    
    












    
    #dossier=open(fileName,'r',encoding='UTF-8')
    #d={}
    #leggo=dossier.readline()
    #split1=leggo.strip().split(',')
    #leggo=dossier.readline()
    #split2=leggo.strip().split(',')
    #if len(split1)==len(split2):
        #num=int(split2[1])
        #if num>=18:
            #d[split2[2]]={split2[0]}
    

            
    
    #dossier.close()
    #return d
            
           
    #devo mettere un ciclo e un readline per far leggere ogni volta di  nuovo
         

            
        
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"] , {'Fisica': [1345, 1753], 'Analisi': [1346], 'Geometria': [1896]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"] , {'Analisi': [1346]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"] , {'Analisi': [1347, 1348], 'Ricerca Operativa': [1347, 1349]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"] , {'Basi di Dati': [1012, 1100], 'Analisi': [1021]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"] , {'Fisica': [1345], 'Fondamenti': [1987], 'Analisi': [1346], 'Geometria': [1896]})

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
