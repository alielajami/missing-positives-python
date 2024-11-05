'''Missing Positives from a List'''

n = int(input("Enter the numbers of digits in the list: "))
list1 = []
for i in range(n):
    num = int(input(f"Enter the number {i+1}: "))
    list1.append(num)

def first_missing_positive(array):
    '''Function to find the first missing positive number'''
    count = 1
    for j in range(len(array)):
        if array[j] == count:
            count += 1
    return count

print("The first missing positive number is: ", first_missing_positive(list1))
