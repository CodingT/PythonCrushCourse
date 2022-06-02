numbers = list(range(1,11))
print(numbers)
for num in numbers:
    if num == 1:
        print(f"\n{num}st")
    elif num == 2:
        print(f"\n{num}nd")
    elif num == 3:
        print(f"\n{num}rd")
    else:
        print(f"\n{num}th")
