car = 'bmw'
print("Is car =='subaru'? I predict True. ")
print(car == 'subaru')

print(car.upper == 'BMW')

print(car.lower == 'bmw')

if car == 'BMW' or car == 'subaru':
    print(car)
    
if car == 'bmw' or car.upper == 'BMW':
    print(f"\ncar low is {car} and car upercase {car.upper}")