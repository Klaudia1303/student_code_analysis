def A_Ex3(fileName):
   ins=set() 
   l2=[]
   f=open(fileName, 'r', encoding='UTF-8')
   s=f.readlines()
   f.close()

   for i in range (1, len(s)):
      riga=(s[i].strip().split(','))
      voto=int(riga[1])
      if(voto>=29):
          materia=riga[2]
          l2.append(materia)
    
   for j in l2:
    if(l2.count(j)>=2):
        ins.add(j)

   return ins

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)