# Start with given list
my_list = [7, 9, 11]
my_list[1] = 17  # a) Modify second entry
my_list.extend([7, 5, 9])  # b) Add numbers
my_list.pop(0)  # c) Remove the first entry
my_list.sort()  # d) Sort the list
my_list *= 2  # e) Double the list
my_list.insert(3, 25)  # f) Insert 25 at index 3
print("g) Final list:", my_list)