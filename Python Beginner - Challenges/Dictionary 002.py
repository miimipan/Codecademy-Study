# 2. Frequency Count

# This next function is similar, but instead of counting the length of each string in the list of strings, we will be counting the frequency of each string. This function will also accept a list of strings as input and return a new dictionary. Here is what we need to do:

# Define the function to accept one parameter for our list of strings
# Create a new empty dictionary
# Loop through every string in the list of strings
# Inside the loop, if the string is NOT already in our dictionary, store the string as a key with a value of 0 in our dictionary. Otherwise, if the string is already in our dictionary, increment the value by 1.
# After the loop, return the new dictionary
#My Solution:
# Write your frequency_dictionary function here:
def frequency_dictionary(words) :
  appear_time={}
  for word in words:
    if word not in appear_time:
      appear_time[word]=0
    appear_time[word] +=1
  return appear_time
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

#CodeCademy Solution:
# def frequency_dictionary(words):
#   freqs = {}
#   for word in words:
#     if word not in freqs:
#       freqs[word] = 0
#     freqs[word] += 1
#   return freqs
