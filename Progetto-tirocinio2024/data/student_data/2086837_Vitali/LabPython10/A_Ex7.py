def A_Ex7(file):
    d={}
    with open(file,'r',encoding="UTF-8") as f:
        _=f.readline()
        for line in f.readlines():
            (first_team, second_team, first_team_score, second_team_score)=line.strip().split(",")
            if first_team not in d or second_team not in d:
                d[first_team]=0
                d[second_team]=0
                
            first_team_score=int(first_team_score)
            second_team_score=int(second_team_score)

            if first_team_score > second_team_score:
                d[first_team]=d.get(first_team,0)+3
            elif second_team_score>first_team_score:
                d[second_team]=d.get(second_team,0)+3
            elif first_team_score==second_team_score:
                d[first_team]=d.get(first_team,0)+1
                d[second_team]=d.get(second_team,0)+1
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
