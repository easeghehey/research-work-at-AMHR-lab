import random

def getSubsetsFromDataSet(filename):
    data = open(filename, "r")
    subsets = []
    costs = []

    for line in data.read().splitlines():
        line = line.lower()
        subsets.append(set(line.split(' ')))
        costs.append(random.randrange(1,10)) # temporary

    return subsets, costs

def exampleSelection(filename, prompt):

    sub, cost = getSubsetsFromDataSet(filename)
    covered, preCovered = set(), set()

    coveredSubsets, totalCost = [], 0

    prompt = set(prompt.split(' '))
    subCopy, costCopy = sub.copy(), cost.copy()

    # print(cost)
    while covered != prompt and subCopy:

        currSub = max(subCopy, key=lambda s: len(s - covered)/costCopy[subCopy.index(s)])
        removeIndex = subCopy.index(currSub)

        covered |= currSub.intersection(prompt)

        if covered != preCovered:
            coveredSubsets.append(currSub)
            totalCost += costCopy[removeIndex]
        
        subCopy.pop(removeIndex)
        costCopy.pop(removeIndex)
        preCovered = covered.copy()

    return coveredSubsets, totalCost if covered == prompt else None


def main():
    datasetFileName = input('Enter name of dataset: ')
    prompt = input('Enter prompt: ')

    try:
        result = exampleSelection(datasetFileName, prompt.lower())

        if not result:
            print('Failed to produce example')
            return
        print(result[0], result[1])

    except:
        print('Failed to run algorithm, ensure your prompt and dataset are input correctly')



main()