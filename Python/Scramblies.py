#https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python


def scramble1(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    k=0
    for c2 in s2:
        l=k
        for c1 in s1:
            if c1 in c2:
                s1.remove(c1)
                k += 1
                break
        if l == k:
            return False
    return True

def scramble(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    for s2 in s1:
        if c1 in c2:
            s1.remove(c1)
            k += 1
            break
    if l == k:
        return False
s1 = 'rkqodlw'
s2 = 'world'
print(scramble(s1,s2))


s1 = 'cedewaraaossoqqyt'
s2 = 'codewars'
#print(scramble(s1,s2))

s1 = 'katas'
s2 = 'steak'
#print(scramble(s1,s2))

s1 = 'scriptjavx'
s2 = 'javascript'
#print(scramble(s1,s2))
