dictionaty = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

def pascal(n):
    res = []
    for i in range(1, n+1):
        tmp = []
        c = 1
        for j in range(1, i+1):
            tmp.append(c)
            c = c * (i - j) // j
        res.append(tmp)
    return res[n-1]

def get_row(n):
    res = pascal(n)
    for i in range(len(res)):
        res[i] *= n
    return res


def encode(str):
    word_dict = str.split(" ")
    res = []
    for word in word_dict:
        word_len = len(word)
        row = get_row(word_len)
        letters = list(word)
        for j in range (word_len):
            letters[j] = dictionaty.__getitem__((dictionaty.index(letters[j]) + row[j]) % 32)
        res.append(letters)
    
    str_res = ""

    for word in res:
        for l in word:
            str_res += l
        str_res += " "

    return str_res

def decode(str):
    word_dict = str.split(" ")
    res = []
    for word in word_dict:
        word_len = len(word)
        row = get_row(word_len)
        letters = list(word)
        for j in range (word_len):
            letters[j] = dictionaty.__getitem__(abs((dictionaty.index(letters[j]) - row[j]) % 32))
        res.append(letters)
    
    str_res = ""

    for word in res:
        for l in word:
            str_res += l
        str_res += " "

    return str_res

def start():
    print("Введите команду:\n[1] - encode\n[2] - decode\n> ", end=' ')
    mode = int(input())
    if (mode == 1):
        str = input()
        print(end='encoded: ')
        print(encode(str.upper()))
    elif (mode == 2):
        str = input()
        print(end='decoded: ')
        print(decode(str.upper()))
    else:
        exit()


start()
