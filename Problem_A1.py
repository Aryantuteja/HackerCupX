def consistent(S):
    con_freq, vow_freq = {}, {}
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in S:
        if i in vowels:
            vow_freq[i] = vow_freq[i] + 1 if vow_freq.get(i) else 1
        else:
            con_freq[i] = con_freq[i] + 1 if con_freq.get(i) else 1
    vow_max = 'b' if vow_freq == {} else max(zip(vow_freq.values(), vow_freq.keys()))[1]
    con_max = 'a' if con_freq == {} else max(zip(con_freq.values(), con_freq.keys()))[1]
    vow_sec = con_sec = 0
    for i in S:
        if i in vowels:
            con_sec += 1
            if i != vow_max:
                vow_sec += 2
        else:
            vow_sec += 1
            if i != con_max:
                con_sec += 2
    return min(vow_sec, con_sec)


f = open("input1.txt", "r")
li = f.readlines()
li = [i[:-1] for i in li]
output = list()
for _ in range(int(li[0])):
    s = li[_+1]
    output.append("Case #"+str(_+1) + ": " + str(consistent(s)))
ans = open("output1.txt","w+")
for i in output:
    ans.write(i+'\n')