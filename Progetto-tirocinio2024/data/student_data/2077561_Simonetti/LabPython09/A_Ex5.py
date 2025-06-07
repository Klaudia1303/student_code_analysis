def A_Ex5(filename,oggetto):
    fin=open(filename,encoding='UTF-8')
    firstRow=fin.readline().strip().split(',')
    linesList=[]
    for line in fin:
        line=line.strip().split(',')
        linesList.append(line)
    index=0
    while index<len(linesList):
        if oggetto in linesList[index]:
            break
        index+=1
    i=0
    maxIncrease=0
    for sales in linesList[index][2:]:
        i+=1
        increase=int(sales)-int(linesList[index][i])
        if increase==0 or maxIncrease==0:
            year=firstRow[1]
        if increase>maxIncrease or increase==maxIncrease:
            maxIncrease=increase
            salesIndex=i+1
            year=firstRow[salesIndex]

            
    

    return int(year)     
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
