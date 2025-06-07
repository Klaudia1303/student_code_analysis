repeat=False
word=input('insert word: ')
for letter in word:
    if 0<word.rfind(letter)-word.find(letter):
        repeat=True
print(repeat)