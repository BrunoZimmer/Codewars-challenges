def valid_parentheses(string):
    resp = 0
    for i in range(len(string)):
        if string[i] == ')' and resp<=0: return False
        elif string[i] == ')': resp-=1
        elif string[i] == '(': resp+=1
    if resp == 0:return True
    else:return False


def valid_parentheses1(string):
    string = re.sub(_regex, '', string)
    while len(string.split('()')) > 1:
        string = ''.join(string.split('()'))
    return string == ''

teste = "hi())("
r = valid_parentheses(teste)
print(r)