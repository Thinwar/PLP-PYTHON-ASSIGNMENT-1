my_list = (10, 20, 30, 40, 50)

# Convert tuple to list
my_list = list(my_list)

# Insert 15 at the second position
my_list.insert(1, 15)

print("The list is:", my_list)
print("The second element is:", my_list[1])

# Sort the list in ascending order
my_list.sort()

print("The list after sorting in ascending order is:", my_list)

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("The index of the value 30 is:", index_of_30)

my_list = [50, 60, 70]

# Remove the last element
my_list.pop()

print("The list after removing the last element is:", my_list)

