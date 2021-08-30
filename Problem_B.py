def fun(C):
    min = len(C[0])
    count = 0
    for i in C:
        if 'O' not in i:
            x = i.count('.')
            if x == 1:
                ind = C.index(i)
                C[ind] = C[ind].replace(".", ",")
            if min > x:
                min = x
                count = 1
            elif min == x:
                count += 1
    C = [''.join(s) for s in zip(*C)]
    for i in C:
        if 'O' not in i:
            x = i.count('.')
            y = i.count(',')
            if x == 0 and y==1:
                continue
            x += y
            if min > x:
                min = x
                count = 1
            elif min == x:
                count += 1
    if count == 0:
        return "Impossible"
    return min, count

f = open("inputB.txt", "r")
li = f.readlines()
li = [i[:-1] for i in li]
output = list()
x = i = 1
while i < len(li):
    C = list()
    n = int(li[i])
    for _ in range(n):
        C.append(li[i+_+1])
    i += n+1
    out = fun(C)
    if out != "Impossible":
        out = str(out[0])+" "+str(out[1])
    output.append("Case #"+str(x) + ": " + out)
    x+=1

ans = open("outputB.txt","w+")
for i in output:
    ans.write(i+'\n')

