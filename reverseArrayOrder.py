#Reverse an order of an array without creating an array

someArray = [0, 1, 10, 4]
length = len(someArray)
iterations = int(length/2)

def revArray():
    for x in range(0, iterations):
        leftSideNum = someArray[x]
        someArray [x]= someArray [(length-1)-(x)]
        someArray [(length-x-1)] = leftSideNum
    print (someArray)
     
revArray()

        
