SYMBLOS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

MAX_KEY_SIZE = len(SYMBLOS)

def getMode():
    while True:
        print('Вы хотите зашифровать или расшифровать текст')
        mode = input().lower()
        if mode in ['зашифровать', 'з', 'расшифровать', 'р']:
            return mode
        else:
            print('Введите "зашифровать" или "з" для зашифровки, "расшифровать" или "р" для расшифровки.')

def getMessage():
    print('Введите текст')
    return input()

def getKey():
    key = 0
    while True:
        print('Введите ключ шифрования (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslateMessage(mode, message, key):
    if mode[0] == 'р':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBLOS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            
            symbolIndex += key

            if symbolIndex >= len(SYMBLOS):
                symbolIndex -= len(SYMBLOS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBLOS)

            translated += SYMBLOS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Преобразованный текст:')
print(getTranslateMessage(mode, message, key))