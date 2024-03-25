class Vehicle:
    def __init__(self,a):
        self.engineSize = ""
    def display(self):
        print("Engine Size: ",self.engineSize)

class Truck(Vehicle):
    def __init__(self,b):
        Vehicle.__init__(self,b)
        self.payLoad = ""
    def display(self):
        print(Vehicle.display(self))
        print("Payload: ",self.payLoad)

class Tanker(Truck):
    def __init__(self,c,function):
        Truck.__init__(self,c)
        self.function = ""
    def display(self):
        print(Truck.display(self))
        print("Funciton: ",self.function)

class TowTruck(Truck):
    def __init__(self,b,cargo):
        Truck.__init__(self,b)
        self.cargo = ""
    def display(self):
        print(Truck.display(self))
        print("Cargo: ",self.cargo)
class TractorTrailer(Truck):
    def __init__(self,a):
        Truck.__init__(self,a)
        self.color = ""
    def display(self):
        print(Truck.display(self))
        print("Color: ",self.color)

class Car(Vehicle):
    def __init__(self,b):
        Vehicle.__init__(self,b)
        self.wheelNum = ""
    def display(self):
        print(Vehicle.display(self))
        print("Wheel Number: ",self.wheelNum)

class SUV(Car):
    def __init__(self,b):
        Car.__init__(self,b)
        self.make = ""
        self.model = ""
        self.year = ""
    def display(self):
        print(Car.display(self))
        print("Make: ",self.make)
        print("Model: ",self.model)
        print("Year: ",self.year)

class Sedan(Car):
    def __init__(self,b):
        Car.__init__(self,b)
        self.make = ""
        self.model = ""
        self.year = ""
    def display(self):
        print(Car.display(self))
        print("Make: ",self.make)
        print("Model: ",self.model)
        print("Year: ",self.year)

class Hatchback(Car):
    def __init__(self,b):
        Car.__init__(self,b)
        self.make = ""
        self.model = ""
        self.year = ""
    def display(self):
        print(Car.display(self))
        print("Make: ",self.make)
        print("Model: ",self.model)
        print("Year: ",self.year)

class MotorBike(Vehicle):
    def __init__(self,b):
        Vehicle.__init__(self,b)
        self.type = ""
    def display(self):
        print(MotorBike.display(self))
        print("Type: :",self.type)

class Chopper(MotorBike):
    def __init__(self,a):
        MotorBike.__init__(self,a)
        self.make = ""
        self.model = ""
        self.year = ""
    def display(self):
        print(MotorBike.display(self))
        print("Make: ", self.make)
        print("Model: ",self.model)
        print("Year: ",self.year)

class Cross(MotorBike):
    def __init__(self,a):
        MotorBike.__init__(self,a)
        self.make = ""
        self.model = ""
        self.year = ""
    def display(self):
        print(MotorBike.display(self))
        print("Make: ",self.make)
        print("Model: ",self.model)
        print("Year: ",self.year)

class Enduro(MotorBike):
    def __init__(self,a):
        MotorBike.__init__(self,a)
        self.make = ""
        self.model = ""
        self.year = ""
    def display(self):
        print(MotorBike.display(self))
        print("Make: ", self.make)
        print("Model: ",self.model)
        print("Year: ", self.year)
#TODO Call/import this in another file, create objects there, then display them all