#Create a function that returns the sum of the values of all even keys in a dictionary.

def sum_even_keys(my_dictionary):
  count = 0
  for i in my_dictionary.keys():
    if i%2 == 0:
      count+= my_dictionary[i]
  return count
# call the function to check the results:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6