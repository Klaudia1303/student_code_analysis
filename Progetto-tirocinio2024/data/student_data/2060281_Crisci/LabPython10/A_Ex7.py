def A_Ex7(fileName):
    diz={}
    f=open(fileName)
    riga1=f.readline()
    righe=f.readlines()
    for i in range(len(righe)):
        riga=righe[i].strip().split(',')
        diz[riga[0]]=0
        diz[riga[1]]=0
    for i in range(len(righe)):
        riga=righe[i].strip().split(',')
        if riga[2]>riga[3]:
            n=diz.get(riga[0])
            diz[riga[0]]=n+3
        elif riga[3]>riga[2]:
            n=diz.get(riga[1])
            diz[riga[1]]=n+3
        else:
            n=diz.get(riga[0])
            diz[riga[0]]=n+1
            n=diz.get(riga[1])
            diz[riga[1]]=n+1
    return (diz)

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
