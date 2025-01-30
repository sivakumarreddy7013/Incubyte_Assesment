1)Create a simple String calculator with a method signature like this:

int add(string numbers)
Input: a string of comma-separated numbers
Output: an integer, sum of the numbers
Examples:

Input: “”, Output: 0
Input: “1”, Output: 1
Input: “1,5”, Output: 6

=============================================

def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    num_list = map(int, numbers.split(","))
    return sum(num_list)

# Test cases
print(add(""))        # Output: 0
print(add("1"))       # Output: 1
print(add("1,5"))     # Output: 6

2) Allow the add method to handle any amount of numbers.
=======================================================
def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    num_list = map(int, numbers.split(","))
    return sum(num_list)

# Test cases
print(add(""))         # Output: 0
print(add("1"))        # Output: 1
print(add("1,5"))      # Output: 6
print(add("1,2,3,4")) # Output: 10

======================================================

3)Allow the add method to handle new lines between numbers (instead of commas). ("1\n2,3" should return 6)
===========================================================
def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    import re
    num_list = map(int, re.split(r"[,
]", numbers))
    return sum(num_list)

# Test cases
print(add(""))         # Output: 0
print(add("1"))        # Output: 1
print(add("1,5"))      # Output: 6
print(add("1,2,3,4")) # Output: 10
print(add("1\n2,3"))  # Output: 6
============================================================================
4)Support different delimiters:

To change the delimiter, the beginning of the string will contain a separate line that looks like this: "//[delimiter]\n[numbers…]". For example, "//;\n1;2" where the delimiter is ";" should return 3.

============================
def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    import re
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]
    else:
        delimiter = r"[,
]"
    
    num_list = map(int, re.split(delimiter, numbers))
    return sum(num_list)

# Test cases
print(add(""))         # Output: 0
print(add("1"))        # Output: 1
print(add("1,5"))      # Output: 6
print(add("1,2,3,4")) # Output: 10
print(add("1\n2,3"))  # Output: 6
print(add("//;\n1;2")) # Output: 3

=======================================================================
5)Calling add with a negative number will throw an exception: "negative numbers not allowed <negative_number>".

If there are multiple negative numbers, show all of them in the exception message, separated by commas.

==================================
def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    import re
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]
    else:
        delimiter = r"[,\n]"
    
    num_list = list(map(int, re.split(delimiter, numbers)))
    negative_numbers = [num for num in num_list if num < 0]
    
    if negative_numbers:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negative_numbers))}")
    
    return sum(num_list)

# Test cases
print(add(""))         # Output: 0
print(add("1"))        # Output: 1
print(add("1,5"))      # Output: 6
print(add("1,2,3,4")) # Output: 10
print(add("1\n2,3"))  # Output: 6
print(add("//;\n1;2")) # Output: 3
try:
    print(add("1,-2,3,-4"))  # Should raise an exception
except ValueError as e:
    print(e)

