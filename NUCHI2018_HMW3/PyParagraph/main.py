#Import Modules
import os
import sys
#Open txt file. "test.tx is the test from the homework readme sample.
# Insert here the txt file path
txtinput = os.path.join('raw_data', 'test.txt')
txtoutput = os.path.join('raw_data', 'testoutput.txt')

with open(txtinput, 'r') as file:
    file_contents = file.read()
    print(file_contents)
    total_char =len(file_contents)
    print("Paragraph Analysis")
    print("------------------")
    print('Approximate word count: ', len(file_contents.split()))
    print('Approximate sentence count: ', file_contents.count('.'))
    
    #Hardcode the extraction of the following special characters in the text[ .,-?!::'><()]
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    count13 = 0
    count14 = 0

    for char in file_contents:
        if char == '.':
            count1 += 1
        if char == ',':
            count2 += 1
        if char == ' ':
            count3 += 1
        if char == '-':
            count4 += 1
        if char == '"':
            count5 += 1
        if char == '?':
            count6 += 1
        if char == '!':
            count7 += 1
        if char == ':':
            count8 += 1
        if char == ';':
            count9 += 1
        if char == "'":
            count10 += 1
        if char == ">":
            count11 += 1
        if char == "<":
            count12 += 1
        if char == "(":
            count13 += 1
        if char == ")":
            count14 += 1
    
    #calculate the amount of special characters in the text
    total_spec_char = count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9 + count10 + count11 + count12 + count13 + count14
    
    #Take out the number of special characters from the total characters
    total_words_only = total_char - total_spec_char 
    
    #Calculate an approximate of letters in a word 
    print('Approximate letter count (per word): ', total_words_only /len(file_contents.split()))
    #Calculate the lenght of a sentence. Assuming each sentence ends in '.'
    print('Average sentence length (in words): ', len(file_contents.split())/file_contents.count('.'))

sys.stdout = open(txtoutput, 'w')
print("Paragraph Analysis")
print("------------------")
print('Approximate word count: ', len(file_contents.split()))
print('Approximate sentence count: ', file_contents.count('.'))
print('Approximate letter count (per word): ',total_words_only / len(file_contents.split()))
print('Average sentence length (in words): ', len(file_contents.split())/file_contents.count('.'))
