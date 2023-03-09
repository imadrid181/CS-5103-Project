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
    for key in list(wc):
        stmt = "{word}: {freq}"
        print(stmt.format(word=key, freq=wc[key]))

print(sys.argv[1])
ws = words(sys.argv[1])
wc = word_count(ws)
print_wc(wc)

