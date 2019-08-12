
import secrets
from secrets import choice
from io import open

verbsFile = open('verbs.txt', 'r', encoding='utf-8')
nounsFile = open('nouns.txt', 'r', encoding='utf-8')

verbsSet = set()

for verb in verbsFile:
    verbsSet.add(verb.rstrip('\n'))

verbsList = list(verbsSet)

nounsSet = set()

for noun in nounsFile:
    nounsSet.add(noun.rstrip('\n'))

nounsList = list(nounsSet)


minsize = 20
maxsize = 25

passwordSize = maxsize + 1

while(passwordSize > maxsize or passwordSize < minsize):
    password = choice(nounsList)
    passwordSize = len(password)
    word = choice(verbsList)
    password += ' ' + word
    word = choice(nounsList)
    password += ' ' + word
    passwordSize = len(password)

print(password, passwordSize)


nounsFile.close()
verbsFile.close()
