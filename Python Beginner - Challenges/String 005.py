# 4. Make Spoonerism

# A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is made when someone says “Belly Jeans” instead of “Jelly Beans”. We are going to make a function that is similar, but instead of using the first syllable, we are going to switch the first character of two words. Here is what we need to do:

# Define the function to accept two parameters for our two words
# Get the first character of the first word and the first character of the second word
# Get the remaining characters of the first word and the remaining characters of the second word.
# Append the first character of the second word to the remaining character of the first word
# Append a space character
# Append the first character of the first word to the remaining characters of the second word.
# Return the result

#My Solution:
# Write your make_spoonerism function here:
def make_spoonerism(wrd1 ,wrd2):
  new_string = wrd2[:1]+ wrd1[1:] + ' ' + wrd1[:1] + wrd2[1:]
  return new_string
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

#CodeCademy Solution:
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]