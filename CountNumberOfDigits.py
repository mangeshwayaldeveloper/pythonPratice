def digits(n):
    count = 0
    num = n
    if n == 0:
        count += 1
        return count
    else:
        count = 0
        while num > 0:  # Complete the while loop condition
            # Complete the body of the while loop. This should include
            # performing a calculation and incrementing a variable in the
            # appropriate order.

            num= int(num / 10)
            count += 1
        return count


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print1