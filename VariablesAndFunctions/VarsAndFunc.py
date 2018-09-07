def print_result(res):
    print("The result is: " + str(res))

def twoNumSubstraction(num1, num2):
    res = num1 - num2
    return res

def unlimited_addition(*nums):
    result = 0;
    for num in nums:
        result = result + num
    return result

res = 0
res = twoNumSubstraction(5,  1)
res = res + unlimited_addition(5, 5, 5, 5)
print_result(res)
