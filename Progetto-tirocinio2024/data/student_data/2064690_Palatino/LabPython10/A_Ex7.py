def A_Ex7(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(file,'r',encoding="UTF-8")
    f.readline()
    diz={}
    for riga in f:
        riga=riga.strip().split(',')
        squadra1=riga[0]
        squadra2=riga[1]
        punti1=riga[2]
        punti2=riga[3]
        if punti1>punti2:
            if squadra1 not in diz and squadra2 not in diz:
                diz[squadra1]=3
                diz[squadra2]=0
            elif squadra1 in diz and squadra2 not in diz:
                diz[squdra1]=int(diz[squadra1])+3
                diz[squadra2]=0
            elif squadra1 not in diz and squadra2 in diz:
                diz[squadra1]=3
                diz[squadra2]=int(diz[squadra2])+0
            elif squadra1 in diz and squadra2 in diz:
                diz[squadra1]=int(diz[squadra1])+3
                diz[squadra2]=int(diz[squadra2])+0
        elif punti2>punti1:
            if squadra1 not in diz and squadra2 not in diz:
                diz[squadra2]=3
                diz[squadra1]=0
            elif squadra1 in diz and squadra2 not in diz:
                diz[squadra1]=diz[squadra1]+0
                diz[squadra2]=3
            elif squadra1 not in diz and squadra2 in diz:
                diz[squadra1]=0
                diz[squadra2]=int(diz[squadra2])+3
            elif squadra1 in diz and squadra2 in diz:
                diz[squadra1]=int(diz[squadra1])+0
                diz[squadra2]=int(diz[squadra2])+3
        elif punti1==punti2:
            if squadra1 not in diz and squadra2 not in diz:
                diz[squadra1]=1
                diz[squadra2]=1
            elif squadra1 in diz and squadra2 not in diz:
                diz[squadra1]=diz[squadra1]+1
                diz[squadra2]=1
            elif squadra1 not in diz and squadra2 in diz:
                diz[squadra1]=1
                diz[squadra2]=int(diz[squadra2])+1
            elif squadra1 in diz and squadra2 in diz:
                diz[squadra1]=int(diz[squadra1])+1
                diz[squadra2]=int(diz[squadra2])+1
    f.close()
    return diz
 
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
