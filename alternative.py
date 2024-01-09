'''
TASK:
  - Write a programe that reads in a string and makes each alternate character
    into an upper case character and each other alternate character a lower 
    case character.

  - Now, try starting with the same string but making each alternate word 
    lower and upper case.
'''

#Every other character in a string is upper case and the rest is lower case 

'''
1. A
sk user to input a sentence and store in variable "sentence"

2. Create a new variable with " " stored, called new_sentence 
(something to refer to throughout the for loop)

3. Create for loop to loop through the sentence and get the 
range of however long the sentence is (determined by len() ),
making every character noted as an index position.

4. Create if statement searching for every index divisable by 2. 
Within this if statement, turn applicable index back into a 
character and make it upper case using .upper()

5. Create an else statement making the remaining characters 
lower case.

6. Print new_sentence
'''

sentence = input("Please enter your sentence: ")
new_sentence = " "

for i in range(len(sentence)):
    if i % 2 == 0:
        new_sentence += sentence[i].upper()
    
    else: 
        new_sentence += sentence[i].lower()

print(new_sentence)

#Each alternate word lower and upper case
'''
1. Create new_sentence_alternate_word with same content as 
new_sentence.

2. Split sentence to sentence into a string, allowing the 
words to be accessed individually, similarly to how indexing
through a string allows for characters to be accessed inividually.

3. Create a for loop and work out length of split_sentence.

4. Create if statement so that if the index is divisable by 2
with the remainder of 1 then that word is upper case and 
add a space at the end.

5. Create else statement to make the remaining words lower 
case and add a space at the end

6. Print new_sentence_alternate_word
'''
new_sentence_alternate_word = " "
split_sentence = sentence.split(" ")

for i in range(len(split_sentence)):
    if i % 2 == 1:
        new_sentence_alternate_word += split_sentence[i].upper() + " "
    
    else:
        new_sentence_alternate_word += split_sentence[i].lower() + " "

print(new_sentence_alternate_word)
