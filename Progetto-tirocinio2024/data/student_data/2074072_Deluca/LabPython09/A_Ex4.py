def A_Ex4(filename,anno):
         f=open(filename)
         s=f.read()
         sclear=s.replace("\n",";")
         l=s.strip().split("\n")
         l1=[]
         for elem in l:
             elem1=elem.split(";")
             l1.append(elem1)
         l2=[]
         for elem in l1:
             elem2=elem[0].split(",")
             l2.append(elem2)
         i=0
         n=1
         while n<len(l2[0]):
             if int(l2[0][n])==anno:
                 i=n
                 break
             n+=1
         oggetto=""
         maxn=0
         n1=1
         while n1<len(l2):
             valore=int(l2[n1][i])
             if valore>maxn:
                 maxn=valore
                 oggetto=l2[n1][0]
             elif valore==maxn:
                 if l2[n1][i]>oggetto:
                     oggetto=l2[n1][i]
                 else:
                     continue
             n1+=1
         return oggetto
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
