def makeMines(mines, li, parent,C, previous):
    key = next(iter(mines))
    for _ in li:
        if key in _ and parent not in _:
            val = _[0] if _[0] != key else _[1]
            mines[key].append({val:[]})
    mines[key].append(previous+C[int(key)-1])
    # print(mines)
    for i in mines[key][:-1]:
        makeMines(i, li, key, C, mines[key][-1])

def findMax(mines, maxValue, parentkey,rootKey, x):
    key = next(iter(mines))
    if parentkey == 1:
        rootKey = x
    li = mines[key]
    if li[-1] > maxValue[0]:
        maxValue[0] = li[-1]
        maxValue[1] = rootKey
    for i in mines[key][:-1]:
        findMax(i, maxValue, parentkey+1,rootKey, x)
        x += 1

f = open("inputC1.txt", "r")
li = f.readlines()
li = [i[:-1] for i in li]
output = list()
x = i = 1
while i < len(li):
    n = int(li[i])
    C = list(map(int, li[i+1].split()))
    mines = {"1":[]}
    gold = []
    i+=2
    for _ in range(n-1):
        a, b = li[i+_].split()
        gold.append([a,b])
    i+=n-1
    makeMines(mines,gold,0,C,-1*C[0])
    maxValue = [0, 0]
    findMax(mines,maxValue, 0, 0, 0)
    firstMax = maxValue[0]
    ind = maxValue[1]
    mines['1'].pop(ind)
    secondMax = 0
    if mines["1"] != []:
        maxValue = [0, 0]
        findMax(mines,maxValue, 0, 0, 0)
        secondMax = maxValue[0]
    result = firstMax + secondMax + C[0]
    output.append("Case #"+str(x) + ": " + str(result))
    x+=1

ans = open("outputC1.txt","w+")
for i in output:
    ans.write(i+'\n')