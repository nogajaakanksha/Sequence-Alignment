import psutil
import os

def writeOutput(l, needleman = 1, output_file="output.txt"):
    s1, s2, penalty, time, memory = [str(i) for i in l]
    with open(output_file, "w") as f:
        s1 = s1[:51] + " " + s1[::-1][:51][::-1] + "\n"
        s2 = s2[:51] + " " + s2[::-1][:51][::-1] + "\n"
        f.write(s1)
        f.write(s2)
        f.write(penalty+"\n")
        f.write(time+"\n")
        f.write(memory)

def readInput(filename):
    l = []
    with open(filename,'r') as f:
        l = f.readlines()

    x = [a.rstrip() for a in l]

    string1 = x[0]
    positions1 = []
    index = 0
    for i in range(1,len(x)):
        if x[i].isnumeric():
            positions1.append(int(x[i]))
        else:
            index = i
            break
    positions2 = []
    string2 = x[index]
    for i in range(index+1, len(x)):
        if x[i].isnumeric():
            positions2.append(int(x[i]))

    return createString(string1, positions1), createString(string2, positions2)

def createString(string, positions):
    prevString = string
    for i in positions:
        currString = prevString
        currString = currString[:i+1]+prevString+currString[i+1:]
        prevString = currString
    assert len(prevString) == 2**len(positions)*len(string)
    return prevString

def memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss
