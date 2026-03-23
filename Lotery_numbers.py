import random

def get_numbers_ticket(min, max, quantity):
    numbers = []
    our_range = range(min, max+1)
    if min in range(1,1000) and max in range(1,1000) and quantity <= len(our_range):
        numbers = random.sample(our_range, quantity)

    else:
        pass
    return sorted(numbers)


print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(-10, 10, 5))
print(get_numbers_ticket(1000, 1200, 10))
print(get_numbers_ticket(10, 4, 5))
print(get_numbers_ticket(10, 14, 6))
