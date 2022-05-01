
#Create a python class called DriveBot  


class DriveBot:
    #feature which allows the use to control multiple robots at once. 
    #The robots have the same latitude and longitude GPS destination coordinates 
    #as well as a setting for disabling them all  
    all_disabled = False
    latitude = -999999
    longitude = -999999
    #keep track of how many robots were created
    robot_count = 0


    def __init__(self, motor_speed =0, direction =180, sensor_range = 10):#create instance variables
      self.motor_speed = motor_speed 
      self.direction = direction
      self.sensor_range = sensor_range
      DriveBot.robot_count +=1
      self.id = DriveBot.robot_count

    def control_bot(self, new_speed, new_direction):#replaces the associated instance variables
      self.motor_speed = new_speed
      self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):#accepts a parameter called new_sensor_range which replaces the sensor_range instance variable
      self.sensor_range = new_sensor_range




robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

#rotate the robot 
robot_1.control_bot(10,180)
robot_1.adjust_sensor(20)
#print(robot_1.motor_speed)
#print(robot_1.direction)
#print(robot_1.sensor_range)

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)
#Change the latitude, longitude, and all_disabled values for all three robots
DriveBot.longitude = 50.0
DriveBot.latitude = -50.0
DriveBot.all_disabled = True

#check robot ids (i.e. how many robots we have)
print(robot_1.id) 
print(robot_2.id)
print(robot_3.id)