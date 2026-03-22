import random

def get_numbers_ticket(min, max, quantity):
    numbers = []
    our_range = range(min, max+1)
    if min >= 1 and max <=1000:
        numbers = random.sample(our_range, quantity)

    else:
        pass
    return numbers


print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(0, 49, 6))
print(get_numbers_ticket(1, 1001, 6))