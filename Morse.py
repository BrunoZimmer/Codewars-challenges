def decodeMorse1(c):
    MORSE_CODE = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', 'SOS':'...---...',
                    '!':'-.-.--'} 
    val = list(MORSE_CODE.values())
    keys = list(MORSE_CODE.keys())

    resp = ''
    esp = 0
    code = ''
    j=0
    
    while c[j]==' ':
        j+=1
    
    for i in range(j,len(c)):
        print(i)
        #print(c[i], i, len(c))
        if c[i] != ' ':
            code += c[i]
            esp = 0            
        if c[i] == ' ' or i == len(c)-1:
            if code != '': resp += keys[val.index(code)]
            code = ''
            esp += 1
        #print(esp)
        if esp == 3: resp += ' '
    return resp

   

def decodeMorse(morseCode):):
    print(letter)
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))

code = ' .... . -.--   .--- ..- -.. .'
print(decodeMorse(code))
