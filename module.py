'''
    Student Name :  LOKENDRA KUMAR AGRAWAL
    Batch : AIML Course from IIK with SimpliLearn
    Project : Module 2 Python Project
    Project Title : Online Car Rental Platform

'''
import datetime
import pprint

#Create a class for renting the cars and define a constructor in it
class RentalCar:
    def __init__(self):
        pass

    def setParameters(self):
        self.hour_value = 0
        self.total_cars = 0
        self.rental_mode_mercedes = 0
        self.hour_base_rent = 0
        self.daily_base_rent = 0
        self.weekly_base_rent = 0
        self.requested_cars_count = 0
        self.time_at_rent = 0
        self.time_at_return = 0
        # Car types
        self.Mercedes = 4
        self.BMW = 3
        self.AUDI = 5
        self.Lamborghini = 2
        self.car_select_status = 1
        self.requested_car = 0

    # Define a method for displaying the available cars
    def available_cars(self):
        print("==========================================================")
        print("Remaining Mercedes = ",self.Mercedes)      
        print("Remaining BMW = ",self.BMW)       
        print("Remaining AUDI = ",self.AUDI)       
        print("Remaining Lamborghini = ",self.Lamborghini)       
        return self.Mercedes + self.BMW + self.AUDI + self.Lamborghini

    # define methods for renting cars on an hourly basis
    def hourlyBasedRent(self):
        if self.requested_cars_count>0 and self.requested_cars_count<self.total_cars:
            self.time_at_rent = datetime.datetime.now();
            self.rental_mode = 'hourly'
            hour_base_rent+=1    
        return self.hour_base_rent

    # define methods for renting cars on an daily basis    
    def dailyBasedRent(self):
        if self.requested_cars_count>0 and self.requested_cars_count<self.total_cars:
            self.time_at_rent = datetime.datetime.now();
            self.rental_mode = 'daily'
            daily_base_rent+=1
        return self.daily_base_rent

    # define methods for renting cars on an weekly basis        
    def weeklyBasedRent(self):
        if self.requested_cars_count>0 and self.requested_cars_count<self.total_cars:
            self.time_at_rent = datetime.datetime.now();  
            self.rental_mode = 'weekly'
            weekly_base_rent+=1
        return self.weekly_base_rent

    def return_the_cars(self): 
        self.time_at_return = datetime.datetime.now()

    def generate_bill(self,requested_car,rental_mode):
        total = 0
        match requested_car:
            case 1: # self.Mercedes
                 if rental_mode == 1:
                     time_diff = 10; # temprary 
                     total = total+5000 * time_diff 
                 elif rental_mode == 2:
                     time_diff = 20; # temprary 
                 elif rental_mode == 3:
                     time_diff = 30; # temprary 
                 else:
                     printf("Rental Mode not selected as per requirement :")
            case 2: # self.Lamborghini
                 total = 6600 *rental_mode
            case 3: # self.AUDI
                 total = 4300 *rental_mode
            case 4: # self.BMW
                 total = 5900 *rental_mode
            case _:
                action-default

        print("Total Time used = ",)
        print("Total Bill  = ",total)
        
        
# Create a class for customers and define a constructor in it.
class Customers(RentalCar):
    
    def __init__(self):
        pass

    def requestingCars(self):
        pass

    def returningCars(self):    
        pass
        

# Define the main method and create objects for both car rental and customer classes
rentalcar = RentalCar()
customer = Customers()
customer.setParameters()

print("Total Types of Car Available : ");
car_types = ["1 for Mercedes", "2 for BMW", "3 for AUDI", "4 for lamborghini"];
car_charges = ["for Mercedes = Rs 5000 per hour", "for BMW = Rs 5900 per hour", "for AUDI = Rs 4300 per hour", "for lamborghini = Rs 6600 per hour"];
pprint.pprint(car_types)
pprint.pprint(car_charges)

# input as a choice for displaying car availability, rental modes, or returning the cars.
requested_car = int(input("Enter your choice for Car "))
customer.requested_car = requested_car
if requested_car == 1:
    print("Total Available Mercedes = ",customer.Mercedes)
    requested_mercedes = int(input("Enter total Mercedes =  "))
    if requested_mercedes <= customer.Mercedes:
        customer.Mercedes-=requested_mercedes
        print("you have selected ",requested_mercedes," Mercedes")
        print("------------Please Select Mode of Rent--------------------")
        print("for hourly basis enter 1 :")
        print("for daily basis enter 2 :")
        print("for weekly basis enter 3 :")
        customer.rental_mode_mercedes = int(input("Please Enter your choice : "))
    else:
        print("You can select maximum Mercedes = ",customer.Mercedes) 
elif requested_car == 2: 
    print("Total Available BMW = ",customer.BMW)
    requested_bmw = int(input("Enter total BMW =  "))
    if requested_bmw <= customer.BMW:
        customer.BMW-=requested_bmw
        print("you have selected ",requested_bmw," BMW")
    else:
        print("You can select maximum BMW = ",customer.BMW) 
elif requested_car == 3:
    print("Total Available AUDI = ",customer.AUDI)
    requested_audi = int(input("Enter total AUDI =  "))
    if requested_audi <= customer.AUDI:
        customer.AUDI-=requested_audi
        print("you have selected ",requested_audi," AUDI")
    else:
        print("You can select maximum AUDI = ",customer.AUDI) 
elif requested_car == 4:
    print("Total Available Lamborghini = ",customer.Lamborghini)
    requested_Lamborghini = int(input("Enter total Lamborghini =  "))
    if requested_Lamborghini <= customer.Lamborghini:
        customer.Lamborghini-=requested_Lamborghini
        print("you have selected ",requested_Lamborghini," Lamborghini")
    else:
        print("You can select maximum Lamborghini = ",customer.Lamborghini) 
else:
    print(" Please give input 1 to 4 only !!!!!!!!!!!")


# status of remainig Car
print("============== Total Car Availalbe together =========================  ",customer.available_cars()) 
customer.generate_bill(customer.requested_car,customer.rental_mode_mercedes)