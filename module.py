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
        self.time_at_rent = 0
        self.time_at_return = 0
        # Car types
        self.Mercedes = 4
        self.BMW = 3
        self.AUDI = 5
        self.Lamborghini = 2
        self.car_select_status = 1
        self.requested_car = 0
        self.requested_mercedes = 0

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
        if self.requested_car>0 and self.requested_car<self.total_cars:
            self.time_at_rent = datetime.datetime.now();
            self.rental_mode = 'hourly'
            hour_base_rent+=1    
        return self.hour_base_rent

    # define methods for renting cars on an daily basis    
    def dailyBasedRent(self):
        if self.requested_car>0 and self.requested_car<self.total_cars:
            self.time_at_rent = datetime.datetime.now();
            self.rental_mode = 'daily'
            daily_base_rent+=1
        return self.daily_base_rent

    # define methods for renting cars on an weekly basis        
    def weeklyBasedRent(self):
        if self.requested_car>0 and self.requested_car<self.total_cars:
            self.time_at_rent = datetime.datetime.now();  
            self.rental_mode = 'weekly'
            weekly_base_rent+=1
        return self.weekly_base_rent

    def return_the_cars(self,rental_time,rental_mode,number_of_cars): 
        # status of remainig Car
        print(f"============== Total Car Availalbe together = {customer.available_cars()} ========================= ") 
        # updating inventary
        if self.requested_car == 1:
            customer.Mercedes += number_of_cars
            # generating bills
            self.generate_bill(self.requested_car,rental_mode)
        elif self.requested_car == 2:
            customer.BMW += number_of_cars
            # generating bills
            self.generate_bill(self.requested_car)            
        elif self.requested_car == 3: 
            customer.AUDI += number_of_cars
            # generating bills
            self.generate_bill(self.requested_car)            
        elif self.requested_car == 4: 
            customer.Lamborghini += number_of_cars
            # generating bills
            self.generate_bill(self.requested_car)            
        else:
            print("")



    def generate_bill(self,requested_car,rental_mode):
        total = 0
        match requested_car:
            # self.Mercedes
            case 1: 
                 # for hourly basis   
                 if rental_mode == 1:
                     rent_time = self.time_at_rent
                     current_time = datetime.datetime.now();
                     
                     time_diff = current_time - rent_time; 
                     hours_difference = time_diff.total_seconds() / 3600
                     total = 5000 * hours_difference 
                     
                     # printing bills data
                     print("Total Time in Hours used = ",hours_difference)
                     print("Total Bill  = ",total)

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
    customer.requested_mercedes = int(input("Enter total Mercedes =  "))
    if customer.requested_mercedes <= customer.Mercedes:
        customer.Mercedes-=customer.requested_mercedes
        print(f"you have selected ",{customer.requested_mercedes}," Mercedes")
        print("------------Please Select Mode of Rent--------------------")
        print("for hourly basis enter 1 :")
        print("for daily basis enter 2 :")
        print("for weekly basis enter 3 :")
        customer.rental_mode_mercedes = int(input("Please Enter your choice : "))
        if customer.rental_mode_mercedes == 1:
            customer.hourlyBasedRent()
        elif customer.rental_mode_mercedes == 2:
            customer.dailyBasedRent()
        elif customer.rental_mode_mercedes == 3:
            customer.weeklyBasedRent()
        else: 
            print("Enter 1, 2 or 3 No other option available !!!!!!!!!!")
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
    

# =========================================================================================
# return the Car/Cars

print("Please return the Car")
car_type = int(input("Enter the Car company name :"))
return_time = datetime.datetime.now()
if car_type == 1:
    customer.return_the_cars(return_time,customer.rental_mode_mercedes,customer.requested_mercedes)
elif car_type == 2:
    customer.return_the_cars(return_time,customer.rental_mode_mercedes,customer.requested_mercedes)
elif car_type == 3:
    customer.return_the_cars(return_time,customer.rental_mode_mercedes,customer.requested_mercedes)
elif car_type == 4: 
    customer.return_the_cars(return_time,customer.rental_mode_mercedes,customer.requested_mercedes)
else:
    print("Try ones again. !!  Enter correct Car type ")
    






