from operator import attrgetter

# Define nested classes
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state
        
class Company:
    def __init__(self, name, city): #issue fixed from (city, name) to (name, city)
        self.name = name
        self.city = city

class Person:
    def __init__(self, name, age, address, company):
        self.name = name
        self.age = age
        self.address = address
        self.company = company

# Sample data
people = [
    Person("Alice", 30, Address("New York", "NY"), Company("Company ABC", "Philadelphia")),
    Person("Bob", 25, Address("Chicago", "IL"), Company("Company DEF", "Nashville")),
    Person("Charlie", 35, Address("Los Angeles", "CA"), Company("Company GHI", "Miami"))
]

# Get sort_key from frontend
# sort_key = "address.city"
sort_key = "company.name"
# sort_key = "address.city"

# Sort based on the dynamic key
sorted_people = sorted(people, key=attrgetter(sort_key))

print([person.name for person in sorted_people])  # Example Output: ['Bob', 'Charlie', 'Alice']

'''
Q: What is the purpose of the attrgetter function in Python?
A: The attrgetter function in Python is used to retrieve attributes from objects.
    It allows you to specify the attribute(s) you want to access, and it returns a callable
    that can be used to extract those attributes from objects. This is particularly useful
    for sorting or filtering collections of objects based on their attributes.
    Time Complexity: The time complexity of using attrgetter is O(1) for accessing a single attribute,
    as it performs a direct attribute lookup. However, when used in sorting or filtering operations,
    the overall time complexity will depend on the specific operations being performed and the size of the data
     being processed.
'''
