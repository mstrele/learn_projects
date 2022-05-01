#write a function called make_spoonerism that takes two strings as parameters named word1 and word2. 
#return the two new words as a single string separated by a space.


def make_spoonerism(word1, word2):
  return word2[0] + word1[1:] +" " + word1[0]+ word2[1:]

# check the outcome:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a