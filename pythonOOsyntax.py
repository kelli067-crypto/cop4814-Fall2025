# Example 2
from pythonSyntax import first_name


class FIUStudent():
    mimimum_grade = 93 #instance variable
    def __init__(self, firstName, lastName, pid, email, grade)
        self.firstName = first_Name
        self.lastName = lastName
        self.pid = pid
        self.email = email
        self.grade = grade

    def current_grade(self):
        return f"{self.firstName.title()}{self.lastName.title()}\'s current grade is {

student1 = FIUStudent("greg","reis",1234,"gmuradre@fiu.edu",86)
print(student1.current_grade())
student2 = FIUStudent("alfredo", "bayuelo",2345,"abayuelo@fiu.edu",95)
print(student2.current_grade())



# Example 3

class Robot(
    def __init__(self, name, weight, battery_life, price):
        self.name = name
        self.weight = weight
        self.battery_life = battery_life
        self.price = price
    def introduce(self)
        return f"I'm{self.name.title()} and my"f" battery last {self.battery_life} hours")

robot1 = Robot("zig",50,4,399,.99)
print(robot1.introduce())

class AquaticRobot(Robot)
    def __init__(self, name, weight, battery_life, price, sensors, motors, isAutonomous)
        super().__init__(name, weight, battery_life,price):
        self.sensors = sensors
        self.motors = motors
        self.isAutonomous = isAutonomous
    def enviroment(self,water):
        return f"I'm {self.name.title()} and I am an aquatic robot that operates in"f"{water} water."

robot2 = AquaticRobot("Echo",170,8,140000, ["temp, "ph"],3,True)



# Example 4

from abc import abstractmethod, ABC

class StreamingService(ABC) # a predifined inherit
    @abstractmethod
    def play(self): #what you need to be a streaming service
        pass
    @abstractmethod
    def add_subscriber(selfself,username):
        pass

    @abstractmethod
    def remove_subscriber(self,username):
        pass

    @abstractmethod
    def display(self):
        pass

class VideoStreamingService(StreamingService):    #is implementing the previous streaming service form before
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.subscribersList = []

    def play(self):
        print("I am a video streaming service and production company")

    def add_subscriber(self,username):
        self.subscribersList.append(username)

    def remove_subscriber(self,username):
        try: #will try to remove and not break if it fails
            self.subscribersList.remove(username)
        except ValueError:
            pass

    def display(self):
        print("I provide tv shows and movies to my subscribers.")

netflix = VideoStreamingService("Netflix",15.99) # needs to implement it so it will not run
netflix.add_subscriber("greg")
print(netflix.subscribersList)