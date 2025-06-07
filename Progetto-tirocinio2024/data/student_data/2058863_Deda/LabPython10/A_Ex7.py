def A_Ex7(file):
    f=open(file,'r',encoding="UTF-8")
    u=f.readlines()
    d={}
    for riga in u:
        x=riga.strip().split(',')
        if x[0]=='Nome_Squadra1':
            continue
        sq1=x[0]
        sq2=x[1]
        gol1=int(x[2])
        gol2=int(x[3])
        k=d.keys()
        if (sq1 not in k) and (sq2 not in k):
            if gol1==gol2:
                d[sq1]=1
                d[sq2]=1
            elif gol1>gol2:
                d[sq1]=3
                d[sq2]=0
            elif gol1<gol2:
                d[sq1]=0
                d[sq2]=3
        elif (sq1 in k) and (sq2 not in k):
            if gol1==gol2:
                d[sq1]+=1
                d[sq2]=1
            elif gol1>gol2:
                d[sq1]+=3
                d[sq2]=0
            elif gol1<gol2:
                d[sq2]=3
        elif (sq1 not in k) and (sq2 in k):
            if gol1==gol2:
                d[sq1]=1
                d[sq2]+=1
            elif gol1>gol2:
                d[sq1]=3
            elif gol1<gol2:
                d[sq1]=0
                d[sq2]+=3
        elif (sq1 in k) and (sq2 in k):
            if gol1==gol2:
                d[sq1]+=1
                d[sq2]+=1
            elif gol1>gol2:
                d[sq1]+=3
            elif gol1<gol2:
                d[sq2]+=3
    f.close()
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
