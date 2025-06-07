def A_Ex7(file):
    fin=open(file,encoding='utf-8')
    partite=[]
    listasquadre=[]
    risultato={}
    for riga in fin:
        partite.append(riga.strip().split(','))
    partite.remove(partite[0])
    for match in partite:
        if int(match[2])>int(match[3]):
            if match[0] not in risultato:
                risultato[match[0]]=0
            if match[1] not in risultato:
                risultato[match[1]]=0
            risultato[match[0]]+=3
        elif int(match[2])==int(match[3]):
            if match[0] not in risultato:
                risultato[match[0]]=0
            if match[1] not in risultato:
                risultato[match[1]]=0
            risultato[match[0]]+=1
            risultato[match[1]]+=1
        else:
            if match[0] not in risultato:
                risultato[match[0]]=0
            if match[1] not in risultato:
                risultato[match[1]]=0
            risultato[match[1]]+=3
    return risultato
                       
        
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, ["partite1.csv"] , {'Chelsea': 3, 'Everton': 3, 'Arsenal': 4, 'Tottenham': 1})
    counter_test_positivi += tester_fun(A_Ex7, ["partite2.csv"] , {'Chelsea': 4, 'Everton': 6, 'Arsenal': 4, 'Tottenham': 2})
    counter_test_positivi += tester_fun(A_Ex7, ["partite3.csv"] , {'Bayern': 4, 'Schalke': 3, 'Amburgo': 4, 'Werder': 1, 'Colonia': 4, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite4.csv"] , {'Bayern': 8, 'Schalke': 6, 'Amburgo': 8, 'Werder': 2, 'Colonia': 8, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite5.csv"] , {'Bayern': 5, 'Schalke': 6, 'Amburgo': 5, 'Werder': 5, 'Colonia': 5, 'Stoccarda': 6})

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
