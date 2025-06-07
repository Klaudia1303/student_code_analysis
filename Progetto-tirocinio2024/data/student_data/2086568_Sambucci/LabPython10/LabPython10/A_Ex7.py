def A_Ex7(file):
    fin=open(file,encoding="UTF-8")
    righe=fin.readlines()
    fin.close()
    diz={}
    for i in range(1,len(righe)):
        riga=righe[i].strip().split(",")
        if riga[0] not in diz:
            diz[riga[0]]=0
        if riga[1] not in diz:
            diz[riga[1]]=0

    for j in range(1,len(righe)):
        risultati=righe[j].strip().split(",")
        if int(risultati[2])>int(risultati[3]):
            diz[risultati[0]]+=3
        elif int(risultati[2])<int(risultati[3]):
            diz[risultati[1]]+=3
        elif int(risultati[2])==int(risultati[3]):
            diz[risultati[0]]+=1
            diz[risultati[1]]+=1
                          
        
    fin.close()
    return diz
        
    

 
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
