import sys

def toDigit(line):
    if isinstance(line, int):  # If the input is already an integer, return it
        return line
    elif line.isdigit():  # If the input is a string containing digits, convert to integer
        return int(line)
    else:
        return line  # Otherwise, return the input unchanged

def plusInLine(line):
    if isinstance(line, str) and "+" in line:
        return True
    else:
        return False

def minusInLine(line):
    if isinstance(line, str) and "-" in line:
        return True
    else:
        return False

def semicolonInLine(line):
    if isinstance(line, str) and ";" in line:  # Check if line is a string and contains ";"
        return True
    else:
        return False
def commaInLine(line):
    if isinstance(line, str) and "," in line:
        return True
    else:
        return False
def dotInLine(line):
    if isinstance(line, str) and "." in line:
        return True
    else:
        return False
def dollarInLine(line):
    if isinstance(line, str) and "$" in line:
        return True
    else:
        return False
def hashInLine(line):
    if isinstance(line, str) and "#" in line:
        return True
    else:
        return False
def atInLine(line):
    if isinstance(line, str) and "@" in line:
        return True
    else:
        return False
def questionInLine(line):
    if isinstance(line, str) and "?" in line:
        return True
    else:
        return False
def tInLine(line):
    if isinstance(line, str) and "T" in line:
        return True
    else:
        return False
def fInLine(line):
    if isinstance(line, str) and "F" in line:
        return True
    else:
        return False
def exclamationInLine(line):
    if isinstance(line, str) and "!" in line:
        return True
    else:
        return False

# open a file from the command line argument
file = open(sys.argv[1],"r")

#each line in the file will be stored in a list
lineList = [""]

#read each line in the file and store it in the list
for line in file:
    lineList.append(line.strip())

lineList = [toDigit(item) if item.isdigit() else item for item in lineList]

index = 1
returnOfCondition = False

while index < len(lineList):
    
    line = lineList[index]
        
    if semicolonInLine(line):
        parts = line.split(";")
        for part in reversed(parts):
            lineList.insert(index,part)
        lineList.remove(line)
        continue

    if plusInLine(line):
        addTo = toDigit(line.replace("+", ""))
        lineList[addTo] = toDigit(lineList[addTo]) + 1

    if minusInLine(line):
        subTo = toDigit(line.replace("-", ""))
        lineList[subTo] = toDigit(lineList[subTo]) - 1

    if commaInLine(line):
        printTo = toDigit(line.replace(",", ""))
        print(lineList[printTo], end='')
    
    if dotInLine(line):
        printTo = toDigit(line.replace(".", ""))
        print(chr(lineList[printTo]), end='')
    
    if dollarInLine(line):
        line = input()
        lineList.insert(index,toDigit(line))
        lineList.remove("$")
    
    if hashInLine(line):
        indiciesForReplacement = line.split("#")
        for i in range(0, len(indiciesForReplacement)):
            indiciesForReplacement[i] = toDigit(indiciesForReplacement[i])
        lineList[indiciesForReplacement[0]] = lineList[indiciesForReplacement[1]]
    
    if atInLine(line):
        jumpTo = toDigit(line.replace("@", ""))
        index = jumpTo
        continue
    if questionInLine(line):
        indiciesForComparison = line.split("?")
        for i in range(0, len(indiciesForComparison)):
            indiciesForComparison[i] = toDigit(indiciesForComparison[i])
        if lineList[indiciesForComparison[0]] == lineList[indiciesForComparison[1]]:
            returnOfCondition = True
        else:
            returnOfCondition = False
    
    if tInLine(line):
        if returnOfCondition == True:
            jumpTo = toDigit(line.replace("T", ""))
            index = jumpTo
            continue

    if fInLine(line):
        if returnOfCondition == False:
            jumpTo = toDigit(line.replace("F", ""))
            index = jumpTo
            continue
    if exclamationInLine(line):
        exit()
    index += 1