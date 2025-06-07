def A_Ex3(fileName):
    
  f=open(filename,'r',encoding='UTF-8')
  dati=f.readline().strip().split
  d={}
  l=[]
  for riga in f:
      l.append(riga.strip().split())
      for i in range(len(l)):
          matricola=l[1][0]
          voto=int(l[i][1])
          materia=l[i][2]
          if voto>=18 and materia not in d:
              d[materia]=[]
          if voto>=18 and materia in d:
              d[materia].append(int(matricola))
              d[materia].sort()
   return d
   f.close()












###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"] , {'Fisica': [1345, 1753], 'Analisi': [1346], 'Geometria': [1896]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"] , {'Analisi': [1346]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"] , {'Analisi': [1347, 1348], 'Ricerca Operativa': [1347, 1349]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"] , {'Basi di Dati': [1012, 1100], 'Analisi': [1021]})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"] , {'Fisica': [1345], 'Fondamenti': [1987], 'Analisi': [1346], 'Geometria': [1896]})

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
