def in_array(a1, a2):
    resp=[]
    for word1 in a1:
        for word2 in a2:
            if word2.find(word1) != -1:
                resp.append(word1)
                break
    k=0
    while k==0:
        for i in range(len(resp)-1):
            if resp[i] > resp[i+1]:
                j = resp[i]
                resp.remove(j)
                resp.insert(i+1, j)
                k += 1
        if k = 0:
    return resp

    def in_array_certo(array1, array2):
    # your code
    res = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and not a1 in res:
                res.append(a1)
    res.sort()
    return res

a1 = ["live", "arp",  "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1,a2))