def A_Ex7(file):

    f=open(file, encoding="UTF-8")
    ls=[]
    lt=[]
    ds={}
    for i in f:
        i=i.strip().split(",")
        ls.append(i)
    for j in range(1,len(ls)):
        for z in range(0,2):
            if [ls[j][z], 0] not in lt:
                lt.append([ls[j][z], 0])
    for c in range(1,len(ls)):
        if int(ls[c][2])==int(ls[c][3]):
            for p in range(len(lt)):
                if lt[p][0]==ls[c][0]:
                    lt[p][1]=int(lt[p][1])+1
            for o in range(len(lt)):
                if lt[o][0]==ls[c][1]:
                    lt[o][1]=int(lt[o][1])+1
        if int(ls[c][2])>int(ls[c][3]):
            for q in range(len(lt)):
                if lt[q][0]==ls[c][0]:
                    lt[q][1]=int(lt[q][1])+3
        if int(ls[c][2])<int(ls[c][3]):
            for w in range(len(lt)):
                if lt[w][0]==ls[c][1]:
                    lt[w][1]=int(lt[w][1])+3
    for i in range(len(lt)):
        ds[lt[i][0]]=int(lt[i][1])
    f.close()
    return ds

 
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
