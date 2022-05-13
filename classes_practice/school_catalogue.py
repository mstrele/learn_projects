



class School:#creates the School class
  
  
  def __init__(self, name, level, numberOfStudents):#let's us initialise the school properties
    self.name = name  
    self.level = level  
    self.numberOfStudents = numberOfStudents


  def get_name(self):#name_getter
    return self.name 

  
  def get_level(self):#level_getter
    return self.level

  def get_numberOfStudents(self):# number of students getter
    return self.numberOfStudents
    

  def set_num_students(self, new_num):#num of students setter
    self.numberOfStudents = new_num

  def __repr__(self):
    return "A {level} school named {name} with {numberOfStudents} students".format(level = self.level, name = self.name,numberOfStudents = self.numberOfStudents)

# test the class
school1 = School("The best", "high", 2540)
#print(school1)
#print(school1.get_name())
#print(school1.get_level())
#school1.set_num_students(200)
#print(school1.get_numberOfStudents())


class PrimarySchool(School):#creates Primary School class which inherits from School
  
  def __init__(self, name, num_students, pickup_policy):#reinit the Primary School
    super().__init__(name, "primary", num_students)
    self.pickup_policy = pickup_policy
  
  def get_pickup_policy(self):#pickup policy getter
    return self.pickup_policy


  def __repr__(self):#rerp override
    parent_rep = super().__repr__()
    return parent_rep + ". The pickup polity is {pickup_policy}".format(pickup_policy = self.pickup_policy)

#test the class  
testSchool = PrimarySchool("Quiteaschool", 300, "Pickup Allowed")
#print(testSchool.get_pickup_policy())
#print(testSchool)


class HighSchool(School):

  def __init__(self, name, num_students, sports_teams):#add sports teams to High School
    super().__init__(name, "high", num_students)
    self.sports_teams = sports_teams

  def get_sports_teams(self):
    return self.sports_teams

  def __repr__(self):
    parent_rep = super().__repr__()
    return parent_rep + ". There are the following teams in school: {sports_teams}".format(sports_teams = self.sports_teams)

#test the class
c = HighSchool("Super Duper High School", 2, ["Tennis", "Basketball"])
print(c.get_sports_teams())
print(c)