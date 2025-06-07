def A_Ex7(file):
    f=open(file,'r',encoding="utf-8")
    f.readline()
    d={}
    for partita in f:
        ris = partita.strip().split(',')
        team1 = ris[0].strip()
        team2 = ris[1].strip()
        gol1 = int(ris[2])
        gol2 = int(ris[3])
        if gol1 > gol2:
            if team1 not in d and team2 not in d:
                d[team1]=3
                d[team2]=0
            elif team1 in d and team2 not in d:
                x=(d.get(team1))
                x+=3
                d[team1]=x
                d[team2]=0
            elif team1 in d and team2 in d:
                x=(d.get(team1))
                x+=3
                d[team1]=x
            elif team1 not in d and team2 in d:
                d[team1]=3
        elif  gol1 < gol2:
            if team2 not in d and team1 not in d:
                d[team2]=3
                d[team1]=0
            elif team2 in d and team1 in d:
                x=(d.get(team2))
                x+=3
                d[team2]=x
            elif team2 not in d and team1 in d:
                d[team2]=3
            elif team2 in d and team1 not in d:
                x=(d.get(team2))
                x+=3
                d[team2]=x
                d[team1]=0
        elif gol1 == gol2:
            if team1 not in d and team2 not in d:
                d[team1]=1
                d[team2]=1
            elif team1 in d and team2 in d:
                x=(d.get(team1))
                x+=1
                d[team1]=x
                y=(d.get(team2))
                y+=1
                d[team2]=y
            elif team1 in d and team2 not in d:
                d[team2]=1
                x=(d.get(team1))
                x+=1
                d[team1]=x
            elif team1 not in d and team2 in d:
                d[team1]=1
                x=(d.get(team2))
                x+=1
                d[team2]=x
                
    f.close()
    return d


 
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
