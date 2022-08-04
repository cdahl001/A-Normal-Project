#Candice Hall
#CIS 245
#Assignment 7.1
#Virtual Garage

#This program creates a class called vehicle and allows the user to input data for a Car or Pickup. 

#Define the parent class Vehicle
class vehicle:
  def __init__(self):
    self.vehicleOptions = {'make': '', 'model': ''}

  def setMake(self, make):
    self.vehicleOptions['make'] = make

  def setModel(self, model):
    self.vehicleOptions['model'] = model

  def displayOptions(self):
    print("") #Adds a new line to make text easier to read
    print("Vehicle successfully added. Here are the details you entered: ")
    print("Make: {self.vehicleOptions['make']}")
    print("Model: {self.vehicleOptions['model']}")
    print("") #Adds a new line to make text easier to read

#Define the child class Car
class car(vehicle): 
  def __init__(self, vehicleOptions):
    car.__init__(self, vehicleOptions)

  def setDoors(self, doors):
    self.vehicleOptions['doors'] = doors

  def displayOptions(self):
    print("Doors: {self.vehicleOptions['doors']}")   
    

#Define the child class Pickup
class pickup(vehicle): 
  def __init__(self, vehicleOptions):
    car.__init__(self, vehicleOptions)

  def setBedLength(self, bedLength):
    self.vehicleOptions['bedLength'] = bedLength

  def displayOptions(self):
    print("Bed Length: {self.vehicleOptions['bedLength']}")  


#Welcome message, then input and call classes
print("Welcome to the virtual garage. Press 1 to enter details for a car, 2 for a pickup, 3 to exit. ")

#py equivalent of a switch here (aka nested if loop)

#Ran out of time to complete this assignment
#Partial credit is better than no credit! 
#Looks like I got the hard part at least (kinda)
