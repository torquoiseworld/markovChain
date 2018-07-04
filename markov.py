import random

with open('whatWasNeeded.txt','r') as f:
    wordArray = []
    capLetterDict = {}
    wordDict = {}
    for line in f:
        for word in line.split():
           wordArray.append(word)
for i in range(0, len(wordArray)-3):
    if (wordArray[i], wordArray[i+1]) in wordDict:
      wordDict[(wordArray[i], wordArray[i+1])].append(wordArray[i+2])
    else:
      wordDict[(wordArray[i], wordArray[i+1])] = [wordArray[i+2]]
      if (wordArray[i][0].isupper()):
        capLetterDict[(wordArray[i], wordArray[i+1])] = [wordArray[i+2]]


randTuple = random.choice(list(capLetterDict))
outputArr = [randTuple[0], randTuple[1]]
for num in range(0, 100):
  possWordList = wordDict[(outputArr[num], outputArr[num+1])]
  randIndex = random.randint(0, len(possWordList)-1)
  outputArr.append(possWordList[randIndex])
  num += 1
print(*outputArr, sep= ' ')
print()


