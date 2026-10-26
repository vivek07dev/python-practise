num = int(input("Enter a number: "))
original = num
sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit ** 3
    num //= 10

if sum_of_digits == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")