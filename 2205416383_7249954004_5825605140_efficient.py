from IO import readInput, writeOutput, memory
from hershey import hirschberg
from time import time
import sys

if __name__ == "__main__":

    s1, s2 = readInput(sys.argv[1])

    start = time()
    penalty, s_1, s_2 = hirschberg(s1,s2)
    end = time()
    params = [s_1, s_2, penalty, end-start, memory()]
    writeOutput(params, 0, "output.txt")
