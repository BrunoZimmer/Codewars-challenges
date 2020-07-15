def validate_pin(pin):
    try:
        val = str(int(pin))
        if int(pin)>=0:
            for i in range(len(str(pin))):
                if str(pin)[i] == '\n' or str(pin)[i] == '+':return False 
            if str(pin)[0] == 0 and len(str(pin)) == 4: return False
            elif str(pin)[0] == 0 and len(str(pin)) == 6: return False
            elif len(str(pin)) == 4 or len(str(pin)) == 6:return True
            else:return False
        else:return False
    except ValueError:
        return False  

def validate_pin1(pin):
    return len(pin) in (4, 6) and pin.isdigit()

iterable = 123
resp = validate_pin(iterable)
print(resp)

iterable = '09876\n'
resp = validate_pin(iterable)
print(resp)