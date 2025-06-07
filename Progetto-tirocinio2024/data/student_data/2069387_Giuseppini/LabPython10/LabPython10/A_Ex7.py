def A_Ex7(file):
    f=open(file, encoding='utf-8')
    f.readline()
    s=f.read().split('\n')
    d={}
    c=0
    
    for riga in s:
        elem=riga.strip('').split(',')
        if len(elem)==4:
            gol1=int(elem[2])
            gol2=int(elem[3])
            s1=elem[0]
            s2=elem[1]
            if s1 not in d:
                d[s1]=0
            if s2 not in d:
                d[s2]=0
            if gol1>gol2:
                d[s1]=d[s1]+3
            if gol2>gol1:
                d[s2]=d[s2]+3
            if gol1==gol2:
                d[s1]=d[s1]+1
                d[s2]=d[s2]+1
        
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
