# Armstrong number is a number that is equal to the sum of cubes of its digits.

num = int(input("Enter a number:"))
sum = 0
temp = num
while temp>0:

    digit = temp%10
    sum += digit**3
    temp //= 10

if num == sum:
   print(num,"is an Armstrong number")

else:
   print(num,"is not an Armstrong number")

'''
Output Example:
Enter a number:153
153 is an Armstrong number
'''
