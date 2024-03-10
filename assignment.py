numbers = input ("10 , 20 , 30").split()
numbers = [int(num) for num in numbers]
sum_of_num = sum(numbers)
print('sum of numbers:',sum_of_num)



favorite_books = ("The Catcher in the Rye", "To Kill a Mockingbird", "Pride and Prejudice")
for book in favorite_books:
    print(book)


# Storing information about a person in a dictionary
person = {}

# Asking for user input
person["name"] = input("Enter your name: ")
person["age"] = input("Enter your age: ")
person["favorite_color"] = input("Enter your favorite color: ")

# Printing the dictionary
print("Person's Information:")
for key, value in person.items():
    print(key + ":", value)


# Accepting user input to create two sets of integers
set1 = set(input("Enter elements for the first set separated by spaces: ").split())
set2 = set(input("Enter elements for the second set separated by spaces: ").split())

# Creating a new set containing common elements from both sets
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)

# Storing a list of words
words = ["apple", "banana", "orange", "grape", "kiwi", "pineapple"]

# Using list comprehension to filter words with odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)

