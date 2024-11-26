# list is collection of data like grocery ,marks, like

list1 = [1, 2, 3]
print(list1)
print(len(list1))
print(list1[0])
print(list1[1])
print(list1[2])

list2 = [98, "manju", 3.19, "ranju"]
print(list2)
print(len(list2))
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])

list2[0] = "Anushs"
list1[1] = "Kumar"
list2[2] = "5654"

print(list2)

print("------------")

# we can use has itterative
for i in list2:
         print(i)

for i in list1:
         print(i)