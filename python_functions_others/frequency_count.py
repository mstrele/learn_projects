#Write a function that returns a dictionary containing the frequency of each element in words

def frequency_dictionary(words):
  new_dict = {}
  for word in words:
    if word not in new_dict:
      new_dict[word] = 0
    new_dict[word] += 1
  return new_dict
  
# call the function to check the resuts:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}