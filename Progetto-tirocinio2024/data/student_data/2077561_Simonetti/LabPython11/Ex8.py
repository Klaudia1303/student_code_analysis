#import re
def Ex8(file):
    fin=open(file,encoding='UTF-8')
    pattern='[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]'
    finalList=[]
    row=fin.readline()
    months='ABCDEHLMPRST'
    while len(row)>0:
        match=re.search(pattern,row)
        if match:
            finditer=re.finditer(pattern,row,re.IGNORECASE)
            for g in finditer:
                s=''
                year=int(g.group(1))
                month=g.group(2)
                day=int(g.group(3))
                if day>31 and day<=40 or day>71:
                    finalList.append('Giorno errato')
                    break
                elif day>40 and day<=71:
                    day-=40
                if (day>=28 and day<=30 or day>=58 and day<=71) and month=='B':
                    finalList.append('Giorno errato')
                    break
                if month in months:
                    month=months.find(month)+1
                elif month not in months:
                    finalList.append('Mese errato')
                    break
                if year>=21:
                    year+=1900
                else: year+=2000
                if len(str(day))==1:
                    day='0'+str(day)
                if len(str(month))==1:
                    month='0'+str(month)
                s=str(day)+'/'+str(month)+'/'+str(year)
                finalList.append(s)
        else: finalList.append('Codice errato')
        row=fin.readline()
    return finalList            
                    
                    
        
    
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
