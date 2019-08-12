
# will change this to a safe cryptographic lib.
import random
from io import open

file = open('words-list.txt', 'r', encoding='utf-8')

wordsSet = set()

for word in file:
    wordsSet.add(word.rstrip('\n'))

wordsList = list(wordsSet)

minsize = 10
maxsize = 15

passwordSize = maxsize + 1

while(passwordSize > maxsize):
    password = random.choice(wordsList)
    passwordSize = len(password)
    while(passwordSize < minsize):
        word = random.choice(wordsList)
        password += ' ' + word
        passwordSize = len(password)


print(password, passwordSize)

print(wordsSet)

file.close()