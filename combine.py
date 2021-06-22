import csv

def addQuotes(string):
   return("\"" + string + "\"")

reader = csv.reader(open('AllClasses.csv'), delimiter=';')
currSpell = ""
prevRow = []
combinedRow = []
classes = []
condensedSpells = []
allSpells = []
for row in reader:
  allSpells.append(row)

allSpells = sorted(allSpells, key=lambda spell: spell[1])
for row in allSpells:
  if (currSpell != row[1].lower() and currSpell != ""):
    combinedRow = prevRow
    combinedRow[-1] = ', '.join(classes)
    condensedSpells.append(combinedRow)
    classes = []
  prevRow = row
  currSpell = row[1].lower()
  trimmedClass = row[-1].split(" ")
  if (len(classes) == 0):
    classes.append(trimmedClass[0])
  elif (trimmedClass[0] != classes[-1]):
    classes.append(trimmedClass[0])

condensedSpells = sorted(condensedSpells, key=lambda spell: spell[0])
writer = csv.writer(open('condensed.csv', 'w', newline=''), delimiter=";", quotechar='@')
for spell in condensedSpells:
  temp = map(addQuotes, spell)
  writer.writerow(temp)
