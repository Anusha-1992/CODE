for i in range (0,10,1):
    if i == 6:
       print(i)
    else:
       print("no O/P")

# I /  CONDITION  / O/P
#i =0 /
print("------*******________")

for i in range (0,10,1):
    if i == 6:
        print(i) # condtion True i==6 print 6 and exit the loop
    else:
        pass

print("------___________________")

for i in range (0,10,1):
    if i == 6:
        print(i)
    else:
        break
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#break example

for i in range(1,6):
    print(i)
    if i ==4:
        break
    print(i,end='')
