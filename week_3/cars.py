# This is a class to get cars descriptions

class car:
 def _init_(self,model,make,year_of_production,fuel_capacity,color,horse_power):
        self.model = model
        self.make = make
        self.year_of_production = year_of_production
        self.fuel_capacity = fuel_capacity
        self.color = color
        self.horse_power = horse_power
        

 def set_make(self,make):
    print("The car is of {}make" .format(self.make))

 def set_make(self,make):
    self.make = make

 def get_make(self):
    return self.make

my_car = car("Lamborghini" , "urus" ,"2020" ,"5500cc" ,"grey" ,"420hp")
other_car = car("note" , "nissan" ,"2019" ,"5200cc" ,"white" ,"380hp")


my_car.print_make("Lamborghini")
my_car.set_make("Ford")
other_car.set_make("Toyota")

print(my_car.get_make())
print(other_car.get_make())






    