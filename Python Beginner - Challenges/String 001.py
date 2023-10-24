#Count Letter
# Exercise Description : 
# 1.Define the function to accept one parameter — the word whose letters we are counting
# 2.Create a counter to keep track of unique letters
# 3.Loop through every letter in our alphabet string. If the current letter was found in our word, increase our count
# 4.Return the count after looping through all letters.

#My SolutionTechnicaTechnica

def unique_english_letters(word):
  letters = []
  for letter in word:
    if letters.count(letter) == 0:
      letters.append(letter)
  return len(letters)
print(unique_english_letters("mississippil"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

#CodeCademy Solution:
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

