
# will change this to a safe cryptographic lib.
import secrets
from secrets import choice
from io import open

verbsFile = open('verbs.txt', 'r', encoding='utf-8')
thingsFile = open('things.txt', 'r', encoding='utf-8')

verbsSet = set()

for verb in verbsFile:
    verbsSet.add(verb.rstrip('\n') + 's')

verbsList = list(verbsSet)

thingsSet = set()

for thing in thingsFile:
    thingsSet.add(thing.rstrip('\n'))

thingsList = list(thingsSet)


minsize = 20
maxsize = 25

passwordSize = maxsize + 1

while(passwordSize > maxsize or passwordSize < minsize):
    password = choice(thingsList)
    passwordSize = len(password)
    word = choice(verbsList)
    password += ' ' + word
    word = choice(thingsList)
    password += ' ' + word
    passwordSize = len(password)

print(password, passwordSize)


thingsFile.close()
verbsFile.close()