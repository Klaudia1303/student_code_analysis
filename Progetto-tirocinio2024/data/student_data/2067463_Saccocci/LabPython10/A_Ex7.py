def A_Ex7(file):
    f=open(file,'r',encoding='UTF-8')
    prima=f.readline().strip().split()
    l=[]
    d={}
    for riga in f:
        riga=riga.strip().split(',')
        l.append(riga)
    for i in range(len(l)):
        squadra1=l[i][0].strip()
        squadra2=l[i][1].strip()
        gol1=int(l[i][2])
        gol2=int(l[i][3])
        if squadra1 not in d:
            puntisquadra=0
            if gol1>gol2:
                puntisquadra+=3
            elif gol1==gol2:
                puntisquadra+=1
            elif gol1<gol2:
                puntisquadra+=0
            d[squadra1]=puntisquadra
        else:
            puntisquadra=0
            if gol1>gol2:
                puntisquadra+=3
            elif gol1==gol2:
                puntisquadra+=1
            elif gol1<gol2:
                puntisquadra+=0
            d[squadra1]+=puntisquadra
        if squadra2 not in d:
            puntisquadra=0
            if gol2>gol1:
                puntisquadra+=3
            elif gol2==gol1:
                puntisquadra+=1
            elif gol2<gol1:
                puntisquadra+=0
            d[squadra2]=puntisquadra
        else:
            puntisquadra=0
            if gol2>gol1:
                puntisquadra+=3
            elif gol2==gol1:
                puntisquadra+=1
            elif gol2<gol1:
                puntisquadra+=0
            d[squadra2]+=puntisquadra
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
