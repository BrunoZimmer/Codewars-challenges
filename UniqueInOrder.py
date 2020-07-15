def unique(iterable):
    if len(iterable)>0:
        resp = [iterable[0]]
        for i in range(1,len(iterable)): 
            if iterable[i] != iterable[i-1]: 
                resp.append(iterable[i])
    else: resp = []
    return resp



""" iterable = 'AAAABBBCCDAABBB'
print(unique(iterable))

iterable = 'ABBCcAD'
resp = unique(iterable)
print(resp)

iterable = [1,2,2,3,3]
resp = unique(iterable)
print(resp) """

iterable = []
resp = unique(iterable)
print(resp)

