# program to print the number of divsors
def divisors_of_number(number):
    divisor=1
    total=0
    while divisor<number:
        if number%divisor==0:
            total=+divisor
        divisor+=1
    return total

print(divisors_of_number(3))
print(divisors_of_number(12))
print(divisors_of_number(10))