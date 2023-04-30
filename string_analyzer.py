import sys
BLANK = [' ', '\n', '\t']

"""
Output will be the analysis of the given text or the analysis
of the text after replacing all occurances of the given word
with the replacement word.
"""

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
            print(stmt.format(word=key, freq=wc[key]),end=', ')

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

def replace(text, find_word, rep_word):
    word = ''
    updated_text = ''
    for char in text:
        if char not in BLANK:
            word += char
        else:
            if word != '':
                if word.lower() == find_word:
                    updated_text += rep_word
                else:
                    updated_text += word
            word = ''
            updated_text += char
    
    if word != '':
        if word.lower() == find_word:
            updated_text += rep_word
        else:
            updated_text += word
            
    return updated_text

#Uses Replace Function
if len(sys.argv) == 4:
    text = sys.argv[1]
    findWord = sys.argv[2]
    repWord = sys.argv[3]
    print("Original Text")
    print(text)

    updatedText = replace(text, findWord, repWord)
    print("\nUpdated Text:")
    print(updatedText)
    words = words(updatedText)
    wordFrequency = word_count(words)
    lineCount = line_count(updatedText)
    charCount = char_count(updatedText)
    print_analysis(wordFrequency, lineCount, charCount)
#Does Not Use Replace Function
elif len(sys.argv) == 2:
    text = sys.argv[1]
    print(text)

    words = words(text)
    wordFrequency = word_count(words)
    lineCount = line_count(text)
    charCount = char_count(text)    
    print_analysis(wordFrequency, lineCount, charCount)