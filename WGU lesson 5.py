#Stores Python and python as strings.
#Compares the two strings to see if they are equal.
#Converts both strings to lowercase and compares them again.
#Prints the results of each comparison.

str1 = "Python"
str2 = "python"

are_equal = str1 == str2
print(f"Are these equal? {are_equal}")

str1_lower =str1.lower()
str2_lower = str2.lower()
are_lower_equal = str1_lower == str2_lower
print(f"Are the lowercase versions equal? {are_lower_equal}")