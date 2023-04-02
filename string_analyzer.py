import sys
BLANK = [' ', '\n', '\t']

def words(text):
    word = ''
    ws = []

    for c in text:
        if c not in BLANK:
            word += c
        else:
            if word != '':
                ws.append(word.capitalize())
            word = ''

    if word != '': ws.append(word.capitalize())
    return ws

def word_count(ws):
    wc = {}
    for word in ws:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
    return wc

def print_wc(wc):
    print("Frequency of Each Unique Word:")
    list_keys = list(wc)
    for key in list_keys:
        stmt = "{word}: {freq}"
        if key == list_keys[-1]:
            print(stmt.format(word=key, freq=wc[key]))
        else:
            print(stmt.format(word=key, freq=wc[key]), end=", ")

def line_count(text):
    lc = 1
    lc += text.count('\n')
    return lc

def char_count(text):
    cc = 0
    for c in text:
        if c not in BLANK:
            cc += 1
    return cc

def print_analysis(wc, lc, cc):
    print_wc(wc)
    print("Line Count: {lc}".format(lc = lc))
    print("Char Count: {cc}".format(cc = cc))

if(len(sys.argv) == 2):
    text = sys.argv[1]
    print(text)
    ws = words(text)
    wc = word_count(ws)
    lc = line_count(text)
    cc = char_count(text)
    print_analysis(wc, lc, cc)

