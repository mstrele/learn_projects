#Write a function that returns the sum of the values of the dictionary

def sum_values(my_dictionary):
  sum_of = 0
  for val in my_dictionary.values():
    sum_of += val
  return sum_of
# call the function to check the result:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6