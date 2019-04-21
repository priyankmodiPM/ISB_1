output = "r_output.txt"

f = open(output)
lines  = f.readlines()
csv = []
for line in lines:
    splittedLines = line.split("    ")
    for i in range(20):
        for char in splittedLines:
            if char == '':
                splittedLines.remove(char)
    csv.append(splittedLines)
f.close()

for line in csv:
    if len(line) < 2:
        csv.remove(line)
    if len(line) > 2:
        del line[len(line) -1]
    deleteLineNum = line[0].split('"')
    if(len(deleteLineNum) > 1):
        del deleteLineNum[0]
        line[0] = "".join(deleteLineNum)
        print("".join(deleteLineNum))

for line in csv:
    lastF = line[-1]
    if (lastF[-1]) == '\n':
        del line[-1]
    deleteLineNum = line[0].split('"')
    if(len(deleteLineNum) > 1):
        del deleteLineNum[0]
        line[0] = "".join(deleteLineNum)
        print("".join(deleteLineNum))
    for i in range(20):
        for char in line:
            if char == '':
                line.remove(char)
    
for line in csv:
    if len(line) < 2:
        csv.remove(line)