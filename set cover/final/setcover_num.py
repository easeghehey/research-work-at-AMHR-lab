n = int(input('Enter n (range for the universal set): '))
numberOfSets = int(input('How many subsets do you wish to enter? A: '))

i = 0
universe = set([num+1 for num in range(n)])
print(f'Universe set: {universe}')
subsets = []
costs = []

def getSubsetsFromInput(subset):
    res = []
    subset = subset.split(',')
    for item in subset:
        res.append(int(item))
    return res

while i < numberOfSets:

    subs = input(f'Enter subset {i + 1} separated by commas\n')
    while subs in {'', ' '}:
        subs = input(f'Enter subset {i + 1} separated by commas: ')
    currentsubset = (getSubsetsFromInput(subs))

    cost = input(f'Enter the associated cost with set {set(currentsubset)}: ')
    while cost.isalpha() or cost in {'', ' '} or int(cost) < 0:
        cost = input(f'Re-enter the associated cost with set {set(currentsubset)}\nIt cannot be negative: ')

    subsets.append(currentsubset)
    costs.append(int(cost))
    i += 1

print(subsets)
print(costs)

def elementsEqualUniverse():
    elem = set()
    for i in range(len(subsets)):
        for j in range(len(subsets[i])):
            if subsets[i][j] in universe:
                elem.add(subsets[i][j])
            else:
                return False
    return True if len(elem) == len(universe) else False

def setcover(universe, subsets, costs):
    if not elementsEqualUniverse():
        print('Sorry the set elements from the subsets dont match the universal set')
        return None

    sub = [set(x) for x in subsets]

    covered = set()
    cover = []
    cost = 0

    while covered != universe:
        print(covered)
        subset = max(sub, key=lambda s: len(s - covered)/costs[sub.index(s)])
        cover.append(subset)
        cost+=costs[sub.index(subset)]
        covered |= subset
 
    return cover, cost


results = setcover(universe, subsets, costs)
if results:
    print(f'Collection: {results[0]}\nCost: {results[1]}')