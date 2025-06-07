def A_Ex7(file):
    d={}
    f=open(file,"r",encoding="UTF-8")
    f.readline()
    for line in f:
        line=line.strip().split(",")
        line[2]=int(line[2])
        line[3]=int(line[3])
        if line[0] not in d:
            d[line[0]]=0
        if line[1] not in d:
            d[line[1]]=0
        if line[0] not in d and line[2]>line[3] :
            d[line[0]]=3
        if line[0] not in d and line[2]==line[3] :
            d[line[0]]=1
        if line[0] in d and line[2]>line[3]:
            d[line[0]]=d[line[0]]+3
        if line[0] in d and line[2]==line[3]:
            d[line[0]]=d[line[0]]+1
        if line[1] not in d and line[3]>line[2] :
            d[line[1]]=3
        if line[1] not in d and line[2]==line[3] :
            d[line[1]]=1
        if line[1] in d and line[3]>line[2]:
            d[line[1]]=d[line[1]]+3
        if line[1] in d and line[2]==line[3]:
            d[line[1]]=d[line[1]]+1
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

