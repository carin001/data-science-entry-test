class Car:                                    #Create a class named Car
    def __init__(self, make, model, year):    #use __init__() method to assign values to object properties
        self.make = make                      #assign values to make, model, year
        self.model = model
        self.year = year

    def describe_car(self):                   #Create describe_car to return print info
        return (c.make, c.model, c.year)

#c1 = Car("BMW", "Gran Coupe", 2019)         #test out the class parameters
#print(c1.make)
#print(c1.model)
#print(c1.year)

c = Car("Toyota","Corolla",2020) #Create an object c

result = c.describe_car()
print(result)