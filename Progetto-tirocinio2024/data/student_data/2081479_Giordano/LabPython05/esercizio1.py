word1=input('insert word 1: ')
word2=input('insert word 2: ')
if len(word1)==len(word2):
    for scan in range(0,len(word1)):
        print(word1[scan:scan+1])
        print(word2[scan:scan+1])
else:
    print('insert same lenght words')