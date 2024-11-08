limit=int(input("Enter the limit:"))
num=int(input("Enter number:"))
small = num
second_smallest = num
big = num
second_biggest = num
while limit>1:
    num = int(input("Enter number:"))
    if num>big:
        second_biggest = big
        big=num
    if num<small:
        second_smallest = small
        small=num
    limit=limit-1
print("the largest number is", big)
print("the smallest number is",small)
print("second largest is",second_biggest)
print("second smallest is",second_smallest)

