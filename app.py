'''Missing Positives from a List'''

n = int(input("Enter the numbers of digits in the list: ")) # number of digits in the list
list1 = [] # Empty list to store the numbers
for i in range(n): # Taking the numbers from the user
    num = int(input(f"Enter the number {i+1}: "))
    list1.append(num) # Appending the numbers to the list

def first_missing_positive(array):
    '''Function to find the first missing positive number'''
    count = 1 # Count variable to store the positive number
    for j in range(len(array)): # Loop to check the positive number
        if array[j] == count: # If the number is positive
            count += 1 # Increment the count
    return count

print("The first missing positive number is: ", first_missing_positive(list1))
