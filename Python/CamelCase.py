def camel_case(string):
    resp= ''
    if len(string)>0:
        if string[0] != ' ': resp+= string[0].upper()
        for i in range(1, len(string)):
            if string[i-1] == ' ': resp += string[i].upper()
            elif string[i] != ' ': resp += string[i]
    return resp

def camel_case1(string):
    return string.title().replace(" ", "")

def camel_case2(string):
    return ''.join([i.capitalize() for i in string.split()])

def camel_case3(string):
    return ''.join((string.title()).split())

st =  ''
resp = camel_case(st)
print(resp)
    
        