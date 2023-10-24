# 5. Add Exclamation

# Let’s say we are writing a program that displays a large message on a blimp and we need to fill in any missing space if a short phrase is provided. Our function will accept a string and if the size is less than 20, it will fill in the remaining space with exclamation marks until the size reaches 20. If the provided string already has a length greater than 20, then we will simply return the original string. Here are the steps:

# Define the function to accept one parameter for our string
# Loop while the length of our input string is less than 20
# Inside the loop, append an exclamation mark
# Once done, return the result

#My Solution:
# Write your add_exclamation function here:
def add_exclamation(word):
  new_word=word
  for i in range(len(word), 20):
    new_word+='!'
  return new_word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
print(add_exclamation('1234567891234567890'))
# should print Codecademy is the best place to learn

#CodeCademy Solution:
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word