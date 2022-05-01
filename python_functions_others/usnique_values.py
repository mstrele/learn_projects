#Create a function that returns the number of unique values in the dictionary

def unique_values(my_dictionary):
  new_l = []
  for value in my_dictionary.values():
    if value not in new_l:
      new_l.append(value)
  return len(new_l)

# call the function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1