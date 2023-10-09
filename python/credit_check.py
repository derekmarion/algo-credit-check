def credit_check(string):
    array = [int(x) for x in string[::-1]]
    check_digit = array.pop(0)
    array = multiply_even(array)
    array = sum_over_ten(array)
    if (10 - (sum(array) % 10)) % 10 == check_digit:
        return "The number is valid!"
    return "The number is invalid!"

def sum_over_ten(arr):
    i = 0
    for element in arr:
        if element >= 10:
            sum_element = sum([int(char) for char in str(element)])
            arr[i] = sum_element
        i += 1
    return arr

def multiply_even(arr):
    i = 0
    for element in arr:
        if i % 2 == 0:
            arr[i] = element * 2
        i += 1
    return arr