def solution1(n):
    resp=''
    Rom_Num = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    Num = [1, 5, 10, 50, 100, 500, 1000]

    for i in range(len(Rom_Num)-1, -1, -1):
        if n >= Num[i]:
            while n >= Num[i]:
                resp += Rom_Num[i]
                n -= Num[i]
        for j in range(i-1, -1, -1):
            if n >= (Num[i] - Num[j]) and j%2 == 0:
                resp += (Rom_Num[j]) + (Rom_Num[i])
                n -= (Num[i] - Num[j])
    return resp

def Solution_Rec(n):
    Num = [['I', 'V', 'X', 'L', 'C', 'D', 'M'],[1, 5, 10, 50, 100, 500, 1000]]

    if n == 0: return 0
    elif n >= Num: return   + Solution_Rec(n)



n =89
resp = solution(n)
print(resp)