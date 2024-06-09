"""
    Student Name :  LOKENDRA KUMAR AGRAWAL
    Batch : AIML Course from IIK with SimpliLearn
    Project : Module 2 Python Project
    Title : Online Car Rental Platform

"""
import datetime
from datetime import timedelta
import pprint
import math


# Create a class for renting the cars and define a constructor in it
class RentalCar:
    def __init__(self):
        pass

    def setParameters(self):
        self.hour_value = 0
        self.total_cars = 0
        self.rental_mode_mercedes = 0
        self.rental_mode_bmw = 0
        self.rental_mode_audi = 0
        self.rental_mode_lamborghini = 0
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
        self.requested_bmw = 0
        self.requested_audi = 0
        self.requested_lamborghini = 0

    # Define a method for displaying the available cars
    def available_cars(self):
        print("==========================================================")
        print("Remaining Mercedes = ", self.Mercedes)
        print("Remaining BMW = ", self.BMW)
        print("Remaining AUDI = ", self.AUDI)
        print("Remaining Lamborghini = ", self.Lamborghini)
        return self.Mercedes + self.BMW + self.AUDI + self.Lamborghini

    # define methods for renting cars on an hourly basis
    def hourlyBasedRent(self):
        if self.requested_car > 0 and self.requested_car < self.available_cars():
            self.time_at_rent = datetime.datetime.now()
            self.rental_mode = 'hourly'
        else:
            self.hour_base_rent += 1
        return self.time_at_rent

    # define methods for renting cars on a daily basis
    def dailyBasedRent(self):
        if self.requested_car > 0 and self.requested_car < self.total_cars:
            self.time_at_rent = datetime.datetime.now()
            self.rental_mode = 'daily'
            self.daily_base_rent += 1
        return self.daily_base_rent

    # define methods for renting cars on a weekly basis
    def weeklyBasedRent(self):
        if self.requested_car > 0 and self.requested_car < self.total_cars:
            self.time_at_rent = datetime.datetime.now()
            self.rental_mode = 'weekly'
            self.weekly_base_rent += 1
        return self.weekly_base_rent

    def return_the_cars(self, rental_time, rental_mode, number_of_cars):
        # updating inventory
        if self.requested_car == 1:
            self.Mercedes += number_of_cars
            # generating bills
            self.generate_bill(rental_time, self.requested_car, rental_mode)
        elif self.requested_car == 2:
            self.BMW += number_of_cars
            # generating bills
            self.generate_bill(rental_time, self.requested_car, rental_mode)
        elif self.requested_car == 3:
            self.AUDI += number_of_cars
            # generating bills
            self.generate_bill(rental_time, self.requested_car, rental_mode)
        elif self.requested_car == 4:
            self.Lamborghini += number_of_cars
            # generating bills
            self.generate_bill(rental_time, self.requested_car, rental_mode)
        else:
            print("")

        # status of remaining Car
        print(f"============== Total Car Available together = {customer.available_cars()} ========================= ")

    def generate_bill(self, rental_time, requested_car, rental_mode):
        # just adding 1 to check real output.
        total = 0
        match requested_car:
            # self.Mercedes
            case 1:
                # for hourly basis
                if rental_mode == 1:
                    current_time = datetime.datetime.now()
                    current_time = current_time + timedelta(hours=6)

                    print(f" rent_time = {rental_time}")
                    print(f" current_time = {current_time}")

                    time_diff = current_time - rental_time
                    hours_difference = time_diff.total_seconds() / 3600
                    total = 5000 * hours_difference
                    factor = 10
                    math.ceil(total * factor) / factor

                    print("=================================================================================")
                    print("=================================================================================")
                    # printing bills data
                    print("Total Time in Hours used = ", hours_difference)
                    print(f"Total Bill  {total} Rupees")

                elif rental_mode == 2:
                    # daily basis
                    self.number_of_days(rental_time)
                elif rental_mode == 3:
                    # weekly basis
                    self.number_of_weeks(rental_time)
                else:
                    print("Rental Mode not selected as per requirement :")
            case 2:  # self.BMW
                # for hourly basis
                if rental_mode == 1:
                    current_time = datetime.datetime.now()
                    current_time = current_time + timedelta(hours=6)

                    print(f" rent_time = {rental_time}")
                    print(f" current_time = {current_time}")

                    time_diff = current_time - rental_time
                    hours_difference = time_diff.total_seconds() / 3600
                    total = 6600 * hours_difference
                    factor = 10
                    math.ceil(total * factor) / factor

                    print("=================================================================================")
                    print("=================================================================================")
                    # printing bills data
                    print("Total Time in Hours used = ", hours_difference)
                    print(f"Total Bill  {total} Rupees")

                elif rental_mode == 2:
                    # daily basis
                    self.number_of_days(rental_time)
                elif rental_mode == 3:
                    # weekly basis
                    self.number_of_weeks(rental_time)
                else:
                    print("Rental Mode not selected as per requirement :")
            case 3:  # self.AUDI
                # for hourly basis
                if rental_mode == 1:
                    current_time = datetime.datetime.now()
                    current_time = current_time + timedelta(hours=6)

                    print(f" rent_time = {rental_time}")
                    print(f" current_time = {current_time}")

                    time_diff = current_time - rental_time
                    hours_difference = time_diff.total_seconds() / 3600
                    total = 4300 * hours_difference
                    factor = 10
                    math.ceil(total * factor) / factor

                    print("=================================================================================")
                    print("=================================================================================")
                    # printing bills data
                    print("Total Time in Hours used = ", hours_difference)
                    print(f"Total Bill  {total} Rupees")

                elif rental_mode == 2:
                    # daily basis
                    self.number_of_days(rental_time)
                elif rental_mode == 3:
                    # weekly basis
                    self.number_of_weeks(rental_time)
                else:
                    print("Rental Mode not selected as per requirement :")
            case 4:  # self.Lamborghini
                # for hourly basis
                if rental_mode == 1:
                    current_time = datetime.datetime.now()
                    current_time = current_time + timedelta(hours=6)

                    print(f" rent_time = {rental_time}")
                    print(f" current_time = {current_time}")

                    time_diff = current_time - rental_time
                    hours_difference = time_diff.total_seconds() / 3600
                    total = 5900 * hours_difference
                    factor = 10
                    math.ceil(total * factor) / factor

                    print("=================================================================================")
                    print("=================================================================================")
                    # printing bills data
                    print("Total Time in Hours used = ", hours_difference)
                    print(f"Total Bill  {total} Rupees")

                elif rental_mode == 2:
                    # daily basis
                    self.number_of_days(rental_time)
                elif rental_mode == 3:
                    # weekly basis
                    self.number_of_weeks(rental_time)
                else:
                    print("Rental Mode not selected as per requirement :")

    def number_of_days(self,rental_time):
        current_time = datetime.datetime.now()
        current_time = current_time + timedelta(days=6)

        print(f" rent_time = {rental_time}")
        print(f" current_time = {current_time}")

        time_diff = current_time - rental_time
        days_difference = time_diff.days
        total = 50000 * days_difference
        factor = 10
        math.ceil(total * factor) / factor

        print("=================================================================================")
        print("=================================================================================")
        # printing bills data
        print("Total days in used = ", days_difference)
        print(f"Total Bill  {total} Rupees")

    def number_of_weeks(self, rental_time):
        current_time = datetime.datetime.now()
        current_time = current_time + timedelta(weeks=3)

        print(f" rent_time = {rental_time}")
        print(f" current_time = {current_time}")

        time_diff = current_time - rental_time
        days_difference = time_diff.days/7
        total = 500000 * days_difference
        factor = 10
        math.ceil(total * factor) / factor

        print("=================================================================================")
        print("=================================================================================")
        # printing bills data
        print("Total weeks in used = ", days_difference)
        print(f"Total Bill  {total} Rupees")


# Create a class for customers and define a constructor in it.
class Customers(RentalCar):

    def __init__(self):
        super().__init__()

    def requesting_cars(self):
        return int(input("Enter your choice for Car "))


    def returning_cars(self):
        super().return_the_cars(self, self.rental_mode, self.total_cars)
        pass


# Define the main method and create objects for both car rental and customer classes
rental_car = RentalCar()
customer = Customers()
customer.setParameters()

print("Total Types of Car Available : ")
car_types = ["1 for Mercedes", "2 for BMW", "3 for AUDI", "4 for lamborghini"]
car_charges = ["for Mercedes = Rs 5000 per hour", "for BMW = Rs 5900 per hour", "for AUDI = Rs 4300 per hour",
               "for lamborghini = Rs 6600 per hour"]
pprint.pprint(car_types)
pprint.pprint(car_charges)

# input as a choice for displaying car availability, rental modes, or returning the cars.
requested_car = customer.requesting_cars()
customer.requested_car = requested_car
time_at_taken = customer.hourlyBasedRent()

if requested_car == 1:
    print("Total Available Mercedes = ", customer.Mercedes)
    customer.requested_mercedes = int(input("Enter total Mercedes =  "))
    if customer.requested_mercedes <= customer.Mercedes:
        customer.Mercedes -= customer.requested_mercedes
        print(f"you have selected ", {customer.requested_mercedes}, " Mercedes")
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
        print("You can select maximum Mercedes = ", customer.Mercedes)
elif requested_car == 2:
    print("Total Available BMW = ", customer.BMW)
    customer.requested_bmw = int(input("Enter total BMW =  "))
    if customer.requested_bmw <= customer.BMW:
        customer.BMW -= customer.requested_bmw
        print(f"you have selected ", {customer.requested_bmw}, " BMW")
        print("------------Please Select Mode of Rent--------------------")
        print("for hourly basis enter 1 :")
        print("for daily basis enter 2 :")
        print("for weekly basis enter 3 :")
        customer.rental_mode_bmw = int(input("Please Enter your choice : "))
        if customer.rental_mode_bmw == 1:
            customer.hourlyBasedRent()
        elif customer.rental_mode_bmw == 2:
            customer.dailyBasedRent()
        elif customer.rental_mode_bmw == 3:
            customer.weeklyBasedRent()
        else:
            print("Enter 1, 2 or 3 No other option available !!!!!!!!!!")
    else:
        print("You can select maximum BMW = ", customer.BMW)
elif requested_car == 3:
    print("Total Available AUDI = ", customer.AUDI)
    customer.requested_audi = int(input("Enter total AUDI =  "))
    if customer.requested_audi <= customer.AUDI:
        customer.AUDI -= customer.requested_audi
        print("you have selected ", customer.requested_audi, " AUDI")
        print("------------Please Select Mode of Rent--------------------")
        print("for hourly basis enter 1 :")
        print("for daily basis enter 2 :")
        print("for weekly basis enter 3 :")
        customer.rental_mode_audi = int(input("Please Enter your choice : "))
        if customer.rental_mode_audi == 1:
            customer.hourlyBasedRent()
        elif customer.rental_mode_audi == 2:
            customer.dailyBasedRent()
        elif customer.rental_mode_audi == 3:
            customer.weeklyBasedRent()
        else:
            print("Enter 1, 2 or 3 No other option available !!!!!!!!!!")
    else:
        print("You can select maximum AUDI = ", customer.AUDI)
elif requested_car == 4:
    print("Total Available Lamborghini = ", customer.Lamborghini)
    customer.requested_lamborghini = int(input("Enter total Lamborghini =  "))
    if customer.requested_lamborghini <= customer.Lamborghini:
        customer.Lamborghini -= customer.requested_lamborghini
        print("you have selected ", customer.requested_lamborghini, " Lamborghini")
        print("------------Please Select Mode of Rent--------------------")
        print("for hourly basis enter 1 :")
        print("for daily basis enter 2 :")
        print("for weekly basis enter 3 :")
        customer.rental_mode_lamborghini = int(input("Please Enter your choice : "))
        if customer.rental_mode_lamborghini == 1:
            customer.hourlyBasedRent()
        elif customer.rental_mode_lamborghini == 2:
            customer.dailyBasedRent()
        elif customer.rental_mode_lamborghini == 3:
            customer.weeklyBasedRent()
        else:
            print("Enter 1, 2 or 3 No other option available !!!!!!!!!!")

    else:
        print("You can select maximum Lamborghini = ", customer.Lamborghini)
else:
    print(" Please give input 1 to 4 only !!!!!!!!!!!")

# =========================================================================================
# return the Car/Cars

print("Please return the Car")
pprint.pprint(car_types)
car_type = int(input("Enter the Car company name :"))
if car_type == 1:
    customer.return_the_cars(time_at_taken, customer.rental_mode_mercedes, customer.requested_mercedes)
elif car_type == 2:
    customer.return_the_cars(time_at_taken, customer.rental_mode_bmw, customer.requested_bmw)
elif car_type == 3:
    customer.return_the_cars(time_at_taken, customer.rental_mode_audi, customer.requested_audi)
elif car_type == 4:
    customer.return_the_cars(time_at_taken, customer.rental_mode_lamborghini, customer.requested_lamborghini)
else:
    print("Try ones again. !!  Enter correct Car type ")
