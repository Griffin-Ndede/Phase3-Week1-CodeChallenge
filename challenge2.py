#if two arguments are positive and one is negative return true
# if all arguments are negative return false
# if only one argument is positive return false

def positive_numbers(a, b, c):

    #covers a
    if a > 0 and b > 0 and c < 0:
        return True
    elif a < 0 and b > 0 and c > 0:
        return True
    elif a > 0 and b < 0 and c > 0:
        return True
    else:
        return False
    
print(positive_numbers(1,3,6))
print(positive_numbers(1,-3,-6))
print(positive_numbers(-11,3,6))


