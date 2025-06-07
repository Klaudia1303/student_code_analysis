def A_Ex7(file):
    file=open(file,'r',encoding='UTF-8')
    _=file.readline()
    f=file.readlines()
    d={}
    

    for riga in f:
        (squadra1,squadra2,punti1,punti2)=riga.strip().split(",")
        punti1=int(punti1)
        
        if squadra1 not in d or squadra2 not in d:
            d[squadra1]=0
            d[squadra2]=0
  
        if int(punti1)>int(punti2):
            d[squadra1]=d[squadra1]+3
            
        if int(punti1)==int(punti2):
            d[squadra1]=d[squadra1]+1
            d[squadra2]=d[squadra2]+1

   
        if int(punti2)>int(punti1):
            d[squadra2]=d[squadra2]+3
    file.close()
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
