word=input('insexxxxrt word: ')
distance=0
biggestSpace=0
for letter in word:
    if biggestSpace<word.rfind(letter)-word.find(letter):
        biggestSpace=word.rfind(letter)-word.find(letter)
print(biggestSpace)