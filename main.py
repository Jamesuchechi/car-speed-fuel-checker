class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0
    
    def accelerate(self, increase):
        self.speed += increase
        return self.speed
    
class Car(Vehicle):
    # Class method to help initialize and define how car instances should be created.
    def __init__(self, brand, model, fuel= 150):
        super().__init__(brand)
        self.model = model
        self.__fuel = fuel

    def accelerate(self, increase):
        if self.__fuel > 0:
            self.speed += increase
            self.__fuel -= increase // 2
        return self.speed
    
    def get_fuel(self):
        return self.__fuel
    
    def __str__(self):
        return f"{self.brand}{self.model}(Speed: {self.speed}, Fuel: {self.__fuel})"
    
# Initialize an instance of Car object
myCar = Car("Toyota", "Camry")
print(myCar)
myCar.accelerate(20)
print(myCar)
print(myCar.get_fuel())