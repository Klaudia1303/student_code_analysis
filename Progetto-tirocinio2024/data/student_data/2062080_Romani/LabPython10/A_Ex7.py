def A_Ex7(file):

    d={}
    f=open(file,'r',encoding='UTF-8')
    first=f.readline()
    
    for riga in f.readlines():
        (Squadra1,Squadra2,punti1,punti2)=riga.strip().split(',')
        if Squadra1 not in d or Squadra2 not in d:
            d[Squadra1]=0
            d[Squadra2]=0
        if int(punti1)>int(punti2):
           d[Squadra1]=d[Squadra1]+3
        elif int(punti2)>int(punti1):
            d[Squadra2]=d[Squadra2]+3
        elif int(punti2)==int(punti1):
            d[Squadra1]=d[Squadra1]+1
            d[Squadra2]=d[Squadra2]+1


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
