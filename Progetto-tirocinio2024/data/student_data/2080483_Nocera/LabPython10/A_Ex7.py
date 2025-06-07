def A_Ex7(file):
    d={}
    fin=open(file,encoding="UTF-8")
    f1=fin.readline().strip().split(",")
    for riga in fin:
        puntisquadra1=0
        puntisquadra2=0
        r=riga.strip().split(",")
        if int(r[2])>int(r[3]):     #r[2] goal segnati dalla prima squadra r[3] goal segnati dalla seconda
            puntisquadra1+=3
        elif int(r[2])==int(r[3]):
            puntisquadra1+=1
            puntisquadra2+=1
        else:
            puntisquadra2+=3
        if r[0] not in d:
            d[r[0]]= puntisquadra1
        else:
            d[r[0]]=d[r[0]]+ puntisquadra1
        if r[1] not in d:
            d[r[1]]= puntisquadra2
        else:
            d[r[1]]= d[r[1]] + puntisquadra2
    fin.close()
    return d
        
            
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
