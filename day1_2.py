# How often does each number from the left list appear in the right list
# Calculate a total similarity score
# - multiply the number by the number of times it appears in the right list
# - add these numbers up
from collections import defaultdict

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

def similarityScore(leftList, rightList):
    similarityScore = 0
    # Put the count of all numbers into a dictionary
    numberCount = defaultdict(int)
    for num in rightList:
        numberCount[num] += 1

    # Calculate similarity score
    for num in leftList:
        similarityScore += num * numberCount[num]

    return similarityScore

list1, list2 = inputToLists("input.txt")
print(similarityScore(list1, list2))