print("Please enter your dividend")
num = input()
num = int(num)
if num % 4 == 0:
    print("You have chosen an even number that is a multiple of 4. Carry on!")
elif num % 2 == 1:
    print("You have have chosen an odd number as your dividend.")
else:
    print("You have chosen an even number as your dividend.")

print("Please enter a divisor")
check = input()
check = int(check)
    
if num % check == 0:
    print("Congratulations, your dividend is completely divisible by your divisor.")
else:
    print("Too bad, your dividend is not completely divisible by your divisor.")


