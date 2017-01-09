# Three functions that can compute the sum of the numbers in a given list
# using a for-loop, a while-loop and a recursion

inputList = [3, 4, 0, 9, 1, 0]

def simpleSumfunc():
    addeditems = sum(inputList)
    print (addeditems)   
#simpleSumfunc()

def recSumfunc(n):
    if n == 1:
        return (inputList[n -1])
    return (inputList[n-1] + recSumfunc(n -1))     
#recSumfunc(len(inputList))    
#print (recSumfunc(len(inputList)))


def loopfunc():
    total = 0
    for value in (inputList):
         total += value
    print (total)
#loopfunc()



def whileloopfunc():
    x = 0
    addeditems = 0
    length = len(inputList)
    while (x < length):
        addeditems += inputList[x]
        x = x+1
    print (addeditems)
#whileloopfunc()
