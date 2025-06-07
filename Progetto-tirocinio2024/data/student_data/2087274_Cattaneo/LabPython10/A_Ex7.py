def A_Ex7(file):
    f=open(file,'r',encoding='UTF-8')
    f.readline()
    i=set()
    l=[]
    d={}
    for line in f:
        line=line.strip().split(',')
        i.add(line[0])
        i.add(line[1])
        l.append(line)
    for e in i:
        d[e]=0
    for riga in l:
        for key in d:
            if key==riga[0]:
                if int(riga[2])>int(riga[3]):
                    d[key]+=3
                elif int(riga[2])==int(riga[3]):
                    d[key]+=1
            if key==riga[1]:
                if int(riga[3])>int(riga[2]):
                       d[key]+=3
                elif int(riga[2])==int(riga[3]):
                    d[key]+=1
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
