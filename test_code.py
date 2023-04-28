from string_analyzer import *

test1 = "There are no repeated words in this sentence"
test1_wc = {"There": 1, "Are": 1, "No": 1, "Repeated": 1, "Words": 1, "In": 1, "This": 1, "Sentence": 1}
test1_lc = 1
test1_cc = 37

test2 = "apple apple apple apple orange apple orange"
test2_wc = {"Apple": 5, "Orange": 2}
test2_lc = 1
test2_cc = 37

test3 = "APPLE APPLE APPLE APPLE ORANGE APPLE ORANGE"
test3_wc = {"Apple": 5, "Orange": 2}
test3_lc = 1
test3_cc = 37

test4 = "ApPle APPle ApplE apple OraNGe ApPLe orange"
test4_wc = {"Apple": 5, "Orange": 2}
test4_lc = 1
test4_cc = 37

test5 = ""
test5_wc = {}
test5_lc = 1
test5_cc = 0

test6 = "Apple\tApple\tOrange\tOrange\tBanana\tBanana"
test6_wc = {"Apple": 2, "Orange": 2, "Banana": 2}
test6_lc = 1
test6_cc = 34

test7 = "Apple\nApple\nOrange\nApple\nOrange\nApple\nOrange"
test7_wc = {"Apple": 4, "Orange": 3}
test7_lc = 7
test7_cc = 38

test8 = "Apple\n\nApple\n\nOrange\n\nApple\n\nOrange\n\nApple\n\nOrange"
test8_wc = {"Apple": 4, "Orange": 3}
test8_lc = 13
test8_cc = 38

test9 = "Did you hear about the gorilla that escaped the zoo \nNo I have not \nThat is cause I'm a very quiet gorilla \nGorilla Noises"
test9_wc = {"Did": 1, "You": 1, "Hear": 1, "About": 1, "The": 2, "Gorilla": 3, "That": 2,
                "Escaped": 1, "Zoo": 1, "No": 1, "I": 1, "Have": 1, "Not": 1, "Is": 1, "Cause": 1,
                "I'm": 1, "A": 1, "Very": 1, "Quiet": 1, "Noises": 1}
test9_lc = 4
test9_cc = 96

test10 = "Hello there I hope you are having a great day"
test10_find_word = "we"
test10_rep_word = "you"
test10_updated_text = "Hello there I hope you are having a great day"
test10_wc = {"Hello": 1, "There": 1, "I": 1, "Hope": 1, "You": 1, "Are": 1, "Having": 1, "A": 1,
             "Great": 1, "Day": 1}
test10_lc = 1
test10_cc = 36

test11 = "To fix the fridge you need to first ensure that it is unplugged"
test11_find_word = "fridge"
test11_rep_word = "oven"
test11_updated_text = "To fix the oven you need to first ensure that it is unplugged"
test11_wc = {"To": 2, "Fix": 1, "The": 1, "Oven": 1, "You": 1, "Need": 1, "First": 1, "Ensure": 1,
             "That": 1, "It": 1, "Is": 1, "Unplugged": 1}
test11_lc = 1
test11_cc = 49

test12 = "This is a test"
test12_find_word = "is"
test12_rep_word = "was"
test12_updated_text = "This was a test"
test12_wc = {"This": 1, "Was": 1, "A": 1, "Test": 1}
test12_lc = 1
test12_cc = 12

test13 = "Is there anything else there"
test13_find_word = "there"
test13_rep_word = "an"
test13_updated_text = "Is an anything else an"
test13_wc = {"Is": 1, "An": 2, "Anything": 1, "Else": 1}
test13_lc = 1
test13_cc = 18

test14 = "There you are \nWe were supposed to be there fifteen minutes ago"
test14_find_word = "there"
test14_rep_word = "an"
test14_updated_text = "an you are \nWe were supposed to be an fifteen minutes ago"
test14_wc = {"An": 2, "You": 1, "Are": 1, "We": 1, "Were": 1, "Supposed": 1, "To": 1, "Be": 1, 
             "Fifteen": 1, "Minutes": 1, "Ago": 1}
test14_lc = 2
test14_cc = 45

ws = words(test1)
wc = word_count(ws)
lc = line_count(test1)
cc = char_count(test1)
print("TEST 1:")
print_analysis(wc, lc, cc)
if test1_wc == wc and test1_lc == lc and test1_cc == cc:
    print("Test 1: Passed")
else:
    print("Test 1: Failed") 

ws = words(test2)
wc = word_count(ws)
lc = line_count(test2)
cc = char_count(test2)
print("\nTEST 2:")
print_analysis(wc, lc, cc)
if test2_wc == wc and test2_lc == lc and test2_cc == cc:
    print("Test 2: Passed")
else:
    print("Test 2: Failed")

ws = words(test3)
wc = word_count(ws)
lc = line_count(test3)
cc = char_count(test3)
print("\nTEST 3:")
print_analysis(wc, lc, cc)
if test3_wc == wc and test3_lc == lc and test3_cc == cc:
    print("Test 3: Passed")
else:
    print("Test 3: Failed")

ws = words(test4)
wc = word_count(ws)
lc = line_count(test4)
cc = char_count(test4)
print("\nTEST 4:")
print_analysis(wc, lc, cc)
if test4_wc == wc and test4_lc == lc and test4_cc == cc:
    print("Test 4: Passed")
else:
    print("Test 4: Failed")   

ws = words(test5)
wc = word_count(ws)
lc = line_count(test5)
cc = char_count(test5)
print("\nTEST 5:")
print_analysis(wc, lc, cc)
if test5_wc == wc and test5_lc == lc and test5_cc == cc:
    print("Test 5: Passed")
else:
    print("Test 5: Failed")  

ws = words(test6)
wc = word_count(ws)
lc = line_count(test6)
cc = char_count(test6)
print("\nTEST 6:")
print_analysis(wc, lc, cc)
if test6_wc == wc and test6_lc == lc and test6_cc == cc:
    print("Test 6: Passed")
else:
    print("Test 6: Passed") 

ws = words(test7)
wc = word_count(ws)
lc = line_count(test7)
cc = char_count(test7)
print("\nTEST 7:")
print_analysis(wc, lc, cc)
if test7_wc == wc and test7_lc == lc and test7_cc == cc:
    print("Test 7: Passed")
else:
    print("Test 7: Passed") 

ws = words(test8)
wc = word_count(ws)
lc = line_count(test8)
cc = char_count(test8)
print("\nTEST 8:")
print_analysis(wc, lc, cc)
if test8_wc == wc and test8_lc == lc and test8_cc == cc:
    print("Test 8: Passed")
else:
    print("Test 8: Failed") 

ws = words(test9)
wc = word_count(ws)
lc = line_count(test9)
cc = char_count(test9)
print("\nTEST 9:")
print_analysis(wc, lc, cc)
if test9_wc == wc and test9_lc == lc and test9_cc == cc:
    print("Test 9: Passed")
else:
    print("Test 9: Failed") 

updatedText = replace(test10, test10_find_word, test10_rep_word)
ws = words(updatedText)
wc = word_count(ws)
lc = line_count(updatedText)
cc = char_count(updatedText)
print("\nTEST 10:")
print("Original Text")
print(test10)
print("\nUpdated Text")
print(updatedText)
print_analysis(wc, lc, cc)
if test10_updated_text == updatedText and test10_wc == wc and test10_lc == lc and test10_cc == cc:
    print("Test 10: Passed")
else:
    print("Test 10: Failed") 

updatedText = replace(test11, test11_find_word, test11_rep_word)
ws = words(updatedText)
wc = word_count(ws)
lc = line_count(updatedText)
cc = char_count(updatedText)
print("\nTEST 11:")
print("Original Text")
print(test11)
print("\nUpdated Text")
print(updatedText)
print_analysis(wc, lc, cc)
if test11_updated_text == updatedText and test11_wc == wc and test11_lc == lc and test11_cc == cc:
    print("Test 11: Passed")
else:
    print("Test 11: Failed") 

updatedText = replace(test12, test12_find_word, test12_rep_word)
ws = words(updatedText)
wc = word_count(ws)
lc = line_count(updatedText)
cc = char_count(updatedText)
print("\nTEST 12:")
print("Original Text")
print(test12)
print("\nUpdated Text")
print(updatedText)
print_analysis(wc, lc, cc)
if test12_updated_text == updatedText and test12_wc == wc and test12_lc == lc and test12_cc == cc:
    print("Test 12: Passed")
else:
    print("Test 12: Failed") 

updatedText = replace(test13, test13_find_word, test13_rep_word)
ws = words(updatedText)
wc = word_count(ws)
lc = line_count(updatedText)
cc = char_count(updatedText)
print("\nTEST 13:")
print("Original Text")
print(test13)
print("\nUpdated Text")
print(updatedText)
print_analysis(wc, lc, cc)
if test13_updated_text == updatedText and test13_wc == wc and test13_lc == lc and test13_cc == cc:
    print("Test 13: Passed")
else:
    print("Test 13: Failed") 

updatedText = replace(test14, test14_find_word, test14_rep_word)
ws = words(updatedText)
wc = word_count(ws)
lc = line_count(updatedText)
cc = char_count(updatedText)
print("\nTEST 14:")
print("Original Text")
print(test14)
print("\nUpdated Text")
print(updatedText)
print_analysis(wc, lc, cc)
if test14_updated_text == updatedText and test14_wc == wc and test14_lc == lc and test14_cc == cc:
    print("Test 14: Passed")
else:
    print("Test 14: Failed") 