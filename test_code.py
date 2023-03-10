from string_analyzer import *

test1 = "There are no repeated words in this sentence"
test1_output = {"There": 1, "Are": 1, "No": 1, "Repeated": 1, "Words": 1, "In": 1, "This": 1, "Sentence": 1}

test2 = "Apple apple Apple apple Orange Apple orange"
test2_output = {"Apple": 5, "Orange": 2}

test3 = ""
test3_output = {}

test4 = "Apple  apple   Orange  orange \nBanana \nBanana"
test4_output = {"Apple": 2, "Orange": 2, "Banana": 2}

test5 = "Apple apple    orange  apple       orange \nApple \n\nOrange"
test5_output = {"Apple": 4, "Orange": 3}

test6 = "Did you hear about the gorilla that escaped the zoo \nNo I have not \nThat is cause I'm a very quiet gorilla \nGorilla Noises"
test6_output = {"Did": 1, "You": 1, "Hear": 1, "About": 1, "The": 2, "Gorilla": 3, "That": 2,
                "Escaped": 1, "Zoo": 1, "No": 1, "I": 1, "Have": 1, "Not": 1, "Is": 1, "Cause": 1,
                "I'm": 1, "A": 1, "Very": 1, "Quiet": 1, "Noises": 1}

ws = words(test1)
wc = word_count(ws)
passed = str(test1_output == wc)
print("Test 1: " + passed)

ws = words(test2)
wc = word_count(ws)
passed = str(test2_output == wc)
print("Test 2: " + passed)

ws = words(test3)
wc = word_count(ws)
passed = str(test3_output == wc)
print("Test 3: " + passed)

ws = words(test4)
wc = word_count(ws)
passed = str(test4_output == wc)
print("Test 4: " + passed)

ws = words(test5)
wc = word_count(ws)
passed = str(test5_output == wc)
print("Test 5: " + passed)

ws = words(test6)
wc = word_count(ws)
passed = str(test6_output == wc)
print("Test 6: " + passed)