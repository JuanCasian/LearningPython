def addition(*nums):
    result = 0;
    for num in nums:
        result = result + num
    return result

value = addition(5, 6, 3, 8);
if (value <  0):
    print("Error in addition")
elif (value == 0):
    print("Value is zero")
else :
    print ("Nice! now we are printing your numbers!")

for i in range(0, value):
    print (i)

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday!"]

print("Now we are printing the weekdays with their index")
for i, day in enumerate(weekDays):
    print(i, day)

