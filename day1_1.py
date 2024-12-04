# Pair the smallest number in the left list with the next smallest number in the right list, and so on
# Measure how far apart they are 

# Search for minimum number in left_list
# Search for minimum number in right_list
# Find distance between them
# Either skip this number when searching next OR delete minimum number indices from list

list1 = []
list2 = []

def inputToLists(txtFileName):
    txtFile = open(txtFileName)
    for line in txtFile:
        # Copy and pasting the input into a txtFile, and then reading it results in strings like "24234   23432\n"
        # So we need to use string methods to modify this back into a list
        leftElement, rightElement = line.split("   ")
        rightElement = (rightElement.split("\n"))[0]

        list1.append(int(leftElement))
        list2.append(int(rightElement))

    return list1, list2
    


def findDistance(leftList, rightList):
    distance = 0
    while(len(leftList) > 0 or len(rightList) > 0):
        leftMin = min(leftList)
        rightMin = min(rightList)

        leftMinIndex = leftList.index(leftMin)
        rightMinIndex = rightList.index(rightMin)

        #print(f"Left Index: {leftList[leftMinIndex]}, Right Index: {rightList[rightMinIndex]}")
        #print(f"Distance: {abs(leftList[leftMinIndex] - rightList[rightMinIndex])}")
        distance += abs(leftList.pop(leftMinIndex) - rightList.pop(rightMinIndex))

    return distance

list1, list2 = inputToLists("input.txt")
print(findDistance(list1, list2))