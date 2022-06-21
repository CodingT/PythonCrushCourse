from moduleRestaurant import Restaurant

ny_stake = Restaurant('kins', 'stake house')
ny_stake.describe_restaurant()
#ny_stake.open_restaurant()
ny_stake.set_number_served(25)
ny_stake.increment_number_served(20)
print(f"\n  The number of served customers at {ny_stake.restaurant_name} is {ny_stake.number_served} ")