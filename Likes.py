def like(names):
    name = ''
    length = len(names)
    if len(names) > 3:
        for i in range(2, len(names)): 
            names.remove(names[2])

    if len(names) == 0:
        name += 'no one' 
    else:
        for i in range(len(names)):
            if i == (len(names)-1):
                name += names[i]
            elif length >3 and i==2:
                pass
            elif length <= 2:
                name += (names[i] + ' and ')
            elif length == 3 and i == 1:
                name += (names[i] + ' and ')
            else:
                name += (names[i] + ', ')

    if length > 3:
        length -=2
        length = str(length)
        names = name + ' and ' + length + ' others like this'
        print(names)

    elif length >1:
        names = name + ' like this'
        print(names)
    else:
        names = name + ' likes this'
        print(names)
    return names

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)

names = ['Alex', 'Jacob', 'Mark', 'Max']
lik = likes(names)
print(lik)

names = ['Jacob', 'Alex', 'Mark']
lik = likes(names)
print(lik)

names = ['Jacob', 'Alex']
lik = likes(names)
print(lik)

names = ['Jacob']
lik = likes(names)
print(lik)

names = []
lik = likes(names)
print(lik)



