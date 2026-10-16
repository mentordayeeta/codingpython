def find_third_largest(nums):

    first = second = third = 0
    
    for num in nums:
        if num == first or num == second or num == third:
            continue
            
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

    return third

numbers = [12, 45, 12, 9, 56, 90, 56, 23]``
print("Third largest:", find_third_largest(numbers))
