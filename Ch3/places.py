from audioop import reverse


places = ['alps', 'mexico', 'costa rica', 'jamaica', 'dominicana', 'bahamas']

print (f"\n sorted places {sorted(places)}")

print (f"\n reverse sorted {sorted(places, reverse=True)}")


print (f"\noriginal list {places}")


places.reverse()
print( places)

places.sort()
print(f"\noriginal sorted {places}")

places.sort(reverse=True)
print(f"\n reversed sorted alpabetical {places}")
print (f"\ntotal placse to visit: {len(places)}")

print(places[3])