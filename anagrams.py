#anagram
from collections import Counter

def maxAnagramSize(input):
    input=input.split(" ")
    for i in range(len(input)):
        input[i]= ''.join(sorted(input[i]))
    print("sorted : " , str(input))
    freqDict= Counter(input)
    print(dict( freqDict))
    print(max(freqDict.values()))

    
# Driver program
if __name__ == "__main__":
    input='cars bikes arcs steer '
    input=input.strip()
    maxAnagramSize(input)

