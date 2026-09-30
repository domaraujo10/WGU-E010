#Write a Python program that:

#Create two integer variables named a and b. X
#Assign a the value 10 and assign b the value 5. X
#Use a comparison operator to compare a and b. X
#Print the result of the comparison to the screen. X
#Update the value of a using an assignment operator so that a increases by 3.
#Create a new variable named result.
#Use logic operators to combine two comparisons:
#Check whether a is greater than b
#Check whether b is less than 10
#Print the value of result.


a = int(input("Input a number for variable a: "))
b = int(input("Input a number for variable b:"))

compare = a > b
print(f"Is a greater than b? {compare}")

a += 3 # Update the value of a to increase by 3
result = (a > b) and (b < 10) # Combine two comparisons using logic operators
print(f"Is a greater than b and is b less than 10? {result}")