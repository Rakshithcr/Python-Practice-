# Second largest in given numbers

num = list(map(int, input("Enter a series of numbers : ").split()))

def sec_big(new):

    largest = float('-inf')
    sec_largest = float('-inf')

    for i in new:
        if i > largest:
            sec_largest = largest
            largest = i
        elif i > sec_largest and i < largest:
            sec_largest = i

    if sec_largest == float('-inf'):
        return None
    else:
        return sec_largest

result = sec_big(num)

if result is None:
    print("No second largest number given..!")
else:
    print("The second largest number is : ",result)