
list1 = [1, 2, 3]
print(list1)

print("elements at index - 0", list1[0])
print("elements at index - 0", list1[1])
print("elements at index - 0", list1[2])

# append () object  to the end of the list
list1.append(4)
list1.append(5)
print(list1)

# extended append a new list extended list

list1.extend([7, 8, 9])
print(list1)

# insert the data  insert(index[0], object )

list1.insert(0,"Raja")
print(list1)
print(len(list1))

list1.insert(0,0)
print(list1)
print(len(list1))