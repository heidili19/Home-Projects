#Write a function that combines two lists by alternatingly taking elements
#For example: given the two lists [a, b, c] and [1, 2, 3]
# the function should return [a, 1, b, 2, c, 3]


letList = ["a", "b", "c"]
numList = ["1", "2", "3"]
test = []
test2 = []


def alternateList():
    lengthlet = len(letList)
    lengthnum = len(numList)
    for value in range(0,lengthlet):
        test.extend(letList[value])
        test.extend(numList[value])
    print (test)
          
alternateList()    
