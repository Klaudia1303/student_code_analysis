def A_Ex7(file):
    f=open(file)
    d={}
    riga=f.readline()
    riga=f.readline()
    dati=riga.strip().split(',')
    while len(riga)>0:
        s1=dati[0]
        s2=dati[1]
        p1=dati[2]
        p2=dati[3]
        
        if int(p1)==int(p2):
            d[s1]=d.get(s1,0)+1
            d[s2]=d.get(s2,0)+1
        elif int(p1)>int(p2):
            d[s1]=d.get(s1,0)+3
            d[s2]=d.get(s2,0)+0
        else:
            d[s1]=d.get(s1,0)+0
            d[s2]=d.get(s2,0)+3
            
        riga=f.readline()
        dati=riga.strip().split(',')
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
