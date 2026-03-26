def is_palindrome(array):
    def check(start, end):
        # Base case: if pointers cross or meet, it's a palindrome
        if start >= end:
            return True
        
        # If elements are different, it's not a palindrome
        if array[start] != array[end]:
            return False
        
        # Recursive call moving towards the center
        return check(start + 1, end - 1)

    return check(0, len(array) - 1)


# Test cases
array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print(is_palindrome(array1))  # True
print(is_palindrome(array2))  # True
print(is_palindrome(array3))  # True
print(is_palindrome(array4))  # False
