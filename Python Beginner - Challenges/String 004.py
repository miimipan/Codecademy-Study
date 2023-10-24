# 3. Reverse

# This one is similar to the last challenge. Instead of selecting every other letter, we want to reverse the entire string. This can be performed in a similar manner, but we will need to modify the range we are using. Here is what we need to do:

# Define the function to accept one parameter for the string
# Create a new empty string to hold the reversed string
# Loop through the input string by starting at the end, and working towards the beginning
# Inside the loop, append the character at the current location to the new string we initialized earlier
# Return the result

#My solution: (Learned rom previous exercise)
# Write your reverse_string function here:
def reverse_string(word):
  reverse_word =''
  for i in range(len(word)-1, -1, -1):
    reverse_word += word[i]
  return reverse_word

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print