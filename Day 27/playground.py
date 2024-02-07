# def add(*args):
#     print(args[0])
#     sum =0
#     for n in args:
#         sum = sum+n
#     return sum

# def calculate(n,**kwargs):
#     print(kwargs)
#     for key,value in kwargs.items():
#         print(key)
#         print(value)
#     n+=kwargs['add']
#     n*=kwargs['multiply']
#     print(n)


# print(add(1,2,3,4,5,6,7,8))
# calculate(2,add=3,multiply=3)

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.year = kwargs.get('year')

car = Car(make='Honda',model='City')
print(car.year)

        