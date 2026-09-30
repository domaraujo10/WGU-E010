#Ask the user for their name using input(), store it in a variable called name, 
# and then print a greeting that includes the name.

name = input("What is your name? ")
print(f"Hello, {name}!")


#Create a list named tasks with three homework tasks: math, science, 
#and reading. Then print the entire list in that order.
tasks = ["math", "science", "reading"]
print(f"Your tasks are: {tasks}")


#Create a variable named total_points with a starting value of 10. Increase the value by 5 using an assignment operator, 
#and then double the result using another assignment operator. Finally, print the final value.
total_points = 10
total_points += 5
total_points *= 2
print(f"Total point after operations: {total_points}")


#Create two numeric variables, a and b, with values 6 and 4. Use arithmetic operators 
#and operator precedence to calculate the result of a + b * 2, 
#store it in a variable named result, and print the value. The result should be 14

a = int(input("Input a number for variable a: "))
b = int(input("Input a number for variable b: "))
result = a + b * 2
print(f"The result of a + b * 2 is: {result}")