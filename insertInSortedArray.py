#Given a sorted array of positive integer with an empty spot at the end
#insert an element in the sorted order


slist = [2, 4, 6, 8, None]

#print (slist[4])

def addList(n):
    length = len(slist) #5
    insertBegList = True
    for x in range ((length -2), -1, -1): #3 to 0
        if n>= slist[x]:
            slist[x+1] = n
            insertBegList = False
            break      
        else:
            slist[x+1] = slist[x]
    if insertBegList == True:
        slist[0] = n
    print (slist)
addList(3)

