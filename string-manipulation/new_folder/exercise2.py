from abc import ABC, abstractmethod
# Method Overriding and Static Methods
class Father:
    x = 10
    y = 20

    @staticmethod
    def add():
        return Father.x + Father.y
    def multiply(self):
        return self.x * self.y
    


class Son(Father):
    a = 30
    b = 40
    def substrac(self):
        return self.b - self.a
    def multiply(self):
        return self.x * self.y * 2


son1 = Son()
father1 = Father()
print(Son.add())
print(son1.substrac())
print(son1.multiply())
print(father1.multiply())


# abstraction using abc module

class Bangladesh(ABC):
    @abstractmethod
    def capital(self):
        pass
    @abstractmethod
    def language(self):
        pass
    @abstractmethod
    def currency(self):
        pass
    @abstractmethod
    def info(self):
        pass

class Dhaka(Bangladesh):
    def capital(self):
        return "Dhaka is the capital of Bangladesh"
    def language(self):
        return "Bengali is the official language of Bangladesh"
    def currency(self):
        return "Taka is the currency of Bangladesh"
    def info(self):
        return "Dhaka is the largest city in Bangladesh"
    
dhaka1 = Dhaka()
print(dhaka1.capital())
print(dhaka1.info())


# polymorphism using method overloading
class MathOperation:
    x = 12
    y = 8
    def add(self, a, b=0):
        return a + b + self.x + self.y
    def multiply(self,*args):
        result = 1
        for num in args:
            result *= num
        return result
math_obj = MathOperation()
print(math_obj.add(10, 20))
print(math_obj.add(15,12))

print(math_obj.multiply(2,3))
print(math_obj.multiply(2,3,4,5))

class Shape:
    def area(self, length, breadth=None):
        if breadth is not None:
            return length * breadth  # Area of rectangle
        else:
            return 3.14 * length ** 2 # Area of circle

shape_obj = Shape()
print(shape_obj.area(5, 10))  # Rectangle area


class Test:
    a = 40
    b= 20
    def display(self,x):
        return self.a + self.b * x
    
test1 = Test()
print(test1.display(2))
print(test1.display(3))


# Access Modifiers in Inheritance
class Car:
    _brand = "Hundai"
    _model = "Sonata"
    __price = 300000
    def _get_details(self):
        return f"brand: {self._brand}, Model: {self._model}, Price: {self.__price}"

class ElectricCar(Car):
    def get_electric_details(self):
        return f"brand: {self._brand}, Model: {self._model}, Type: Electric"
    

electric_car = ElectricCar()
# print(electric_car.get_electric_details())
print(electric_car._get_details())  # not recommended but possible

