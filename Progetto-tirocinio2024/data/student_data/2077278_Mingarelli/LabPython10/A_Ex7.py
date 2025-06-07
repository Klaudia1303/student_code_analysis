def A_Ex7(file):
    f=open(file,encoding='UTF-8')
    f.readline()
    partite=f.readline().strip().split(',')
    d={}
    while len(partite)>0 and partite!=['']:
        casa=partite[0]
        ospite=partite[1]
        gol1=int(partite[2])
        gol2=int(partite[3])
        if casa not in d:
            d[casa]=0
        if ospite not in d:
            d[ospite]=0
        if gol1>gol2:
            d[casa]+=3
        elif gol2>gol1:
            d[ospite]+=3
        elif gol2==gol1:
            d[casa]+=1
            d[ospite]+=1
        partite=f.readline().strip().split(',')
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
