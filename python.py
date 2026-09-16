# Lists uses [],  allowing items to be added, removed, or changed, making them helpful in organizing information that may grow or update.
files = ["report.txt", "data.csv", "summary.docx", "presentation.pptx", "image.png"]
print(files)
print(files[0])  # Accessing the first file in the list

# dictionaries use {}, nable you to label and access data clearly, making them useful for storing structured information, such as settings or user details.
device = {"ipaddress": "192.168.1.1", "status": "online"}
print(device)

#Tuples use (), useful for information that should stay fixed, such as coordinates or device settings.
fruits = ("apple", "banana", "cherry", "grape")
print(fruits)

# Sets use {},  you need to quickly check membership or avoid duplicate values in tasks such as filtering data. Sets do not support indexing.
colors = {"red", "green", "blue"}
print(colors)
#or
active_ports = {22, 80, 443}
print(active_ports)


#You can you the len() function to determine the number of items in a list, dictionary, tuple, or set.
count = len(active_ports)
print(count) # Output: 3
#You can also use len like this
print(len(fruits)-1) # Output: 3

# the Pop() method removes and returns the last item in a list, allowing you to retrieve and remove items from the end of the list.
removed_files = files.pop()
print(removed_files)  # Output: presentation.pptx
print(files)  # Output: ['report.txt', 'data.csv', 'summary.docx']

#you can also do this
removed = files.pop(1)  # Removes the second item (index 1)
print(files)  # Output: ['report.txt', 'summary.docx']
print(removed)  # Output: data.csv

#remove() method removes the first occurrence of a specified value from a list, allowing you to delete items based on their content rather than their position.
files.remove("summary.docx")
print(files)  # Output: ['report.txt']

#index() method returns the index of the first occurrence of a specified value in a list, allowing you to find the position of an item within the list.
position = fruits.index("cherry")  # Returns the index of "cherry" in the fruits tuple
print(position)  # Output: 2

#you can extend this code by doing this
item = fruits[position]  # Accessing the item at the found index
print(item)  # Output: cherry


#You can also add items to a list, but itll add it to the END of the list
fruits.append("Dragon Fruit")
print(fruits)

#The sort() method is a list method in Python that arranges the items in a list in a specific order. By default, 
#it sorts values in ascending order, such as alphabetically for strings or from smallest to largest for numbers. It changes the original list rather than creating a new one.
devices = ['Iphone', 'Tablet', 'Computer', 'Printer']
devices.sort()
print(devices)

#you can also do them reverse by adding doing sort(reverse=True)
devices.sort(reverse=True)
print(devices


#The get() code s a dictionary method that retrieves the value for a specified key. 
#It works like using square brackets, but it is safer because it does not cause an error if the key is missing. Instead, it returns None or a default value you choose.
phones = {
  "Apple": "Iphone 8",
  "Apple1": "Iphone 11", 
  "Samsung": "Samsung Galaxy Flip",
  "Samsung1": "Samsung Galaxy 8"}
result = phones.get("Apple1")
print(result)

#keys() is a dictionary method in Python that returns a view object containing all the keys in the dictionary. 
#This view updates automatically if the dictionary changes. It is often used when you want to loop through keys or see what information the dictionary stores.
print(phones.keys())

#keys() is a dictionary method in Python that returns a view object containing all the keys in the dictionary. 
#This view updates automatically if the dictionary changes. It is often used when you want to loop through keys or see what information the dictionary stores.
print(phones.keys())

#values() is a dictionary method in Python that returns a view object containing all the values stored in the dictionary. 
#This view updates automatically if the dictionary changes. It is useful when you want to examine or loop through only the values without needing the keys.
print(phones.values())

#items() is a dictionary method in Python that returns a view object containing all key-value pairs in the dictionary as tuples. Each tuple has the form (key, value).
print(phones.items())

#You can add or modify dictionary elements by assigning a value to a key using square brackets. If the key already exists, its value is updated. If the key does not exist, a new key-value pair is created.
phones["Hawaii"] = "Hawaii Fold"  #adds new key
phones["Apple"] = "Iphone Duo" #updates key
