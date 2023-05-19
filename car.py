#%%
#sneakcase
#for variables we separate words using underscore
name_of_person = "JJ"

# camelcase for names of classes
class Car:
    pass
#The pass statement is used as a placeholder for future code

#creating instances/objects of class
car1 = Car()
car2 = Car()

#print(type(car1))
print(car1 == car2)
# it's false because objects of classes are always 
# compared to by their reference. will see if address 
# is the same and it's not because they are in different 
# places in memory
#%%

lst = [1, 2, 3]

print(type(lst))
# %%

class Car:
    # way of writing things with two underscore called 
    # "dunder"
    # this is the constructor, where you name attributes
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

bmw_m3 = Car("BMW", "M3", "Blue")
ford_mustang = Car("Ford", "Mustang", "Yellow")

print(bmw_m3.brand)
print(ford_mustang.color)
# %%

class Car:
    # way of writing things with two underscore called 
    # "dunder"
    # this is the constructor, where you name attributes
    def __init__(self, brand, model, color):
    #if type(brand) != str:
    #raise Exception("brand must be a string")
    #if brand != "Ford" or brand != "BMW":
    #raise Exception()
    #or create an array of allowed brands like this
    #allowed_brands = ["Ford", "BMW"]
    #if brand not in allowed_brands:

        self.brand = brand
        self.model = model
        self.color = color

bmw_m3 = Car("BMW", "M3", "Blue")
ford_mustang = Car("Ford", "Mustang", "Yellow")

print(bmw_m3.brand)
# %%
# this is raising an exception
print(1 / 0)
# %%

# list can change size and have ordering
[1, 3, 34]

# tuples cannot grow or shrink in size
(1, 2, 3, 4)

# sets: no repetition, fast check of existence in the set
{1, 2, 3, 4}
# %%

class Clock:
    def __init__(self, hours, minutes):

        if minutes not in range(0, 60):
            raise Exception("minutes must be 0-59")

        if hours not in range(0, 24):
            raise Exception("hours must be 0-24")

        self.hours = hours
        self.minutes = minutes

blue_clock = Clock (22, 30)
yellow_clock = Clock (12, 24)

print(blue_clock.minutes)


# %%

class Clock:
    def __init__(self, hours, minutes):

        if minutes not in range(0, 60):
            raise Exception("minutes must be 0-59")

        if hours not in range(0, 24):
            raise Exception("hours must be 0-24")

        self.hours = hours
        self.minutes = minutes

    def sound_alarm(self):
        return ("ALAAARRM")

blue_clock = Clock (22, 30)
yellow_clock = Clock (12, 24)

print(blue_clock.sound_alarm())
# %%

class Clock:
    def __init__(self, hours, minutes):

        if minutes not in range(0, 60):
            raise Exception("minutes must be 0-59")

        if hours not in range(0, 24):
            raise Exception("hours must be 0-24")

        self.hours = hours
        self.minutes = minutes
        self.illuminated = False

    def sound_alarm(self):
        return ("ALAAARRM")
    
    def turn_light_on(self):
        self.illuminated = True
    
    def turn_light_off(self):
        self.illuminated = False

blue_clock.sound_alarm()
yellow_clock.turn_light_on()

print(blue_clock.illuminated)


# %%
# increment by 1 tick SIMPLE

class Clock:
    def __init__(self, hours, minutes):

        self.hours = hours
        self.minutes = minutes

    def tick(self):
        self.minutes = self.minutes +1

clock_1 = Clock(12, 43)

clock_1.tick()

print(str(clock_1.hours) + ":" + str(clock_1.minutes))

# %%

# %%

class Clock:
    def __init__(self, hours, minutes):

        self.hours = hours
        self.minutes = minutes

    def tick(self):
        self.minutes = self.minutes +1

clock_1 = Clock(12, 43)

#iterate 10 times by 1 tick
for n in range(10):
    clock_1.tick()

clock_1.tick()

print(str(clock_1.hours) + ":" + str(clock_1.minutes))
# %%

# %%

class Clock:
    def __init__(self, hours, minutes):

        self.hours = hours
        self.minutes = minutes

    def tick_hours(self):
        self.hours = self.hours +1
        if self.hours >= 24:
            self.hours = 0

    def tick(self):
        self.minutes = self.minutes +1
        if self.minutes >= 60:
            self.minutes = 0
            self.tick_hours()

clock_1 = Clock(12, 43)

import time

while True:
    time.sleep(1)
    clock_1.tick()
    print(str(clock_1.hours) + ":" + (str(clock_1.minutes)))
# %%
