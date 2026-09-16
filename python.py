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