import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create an instance of the class
person = Person("Alice", 30)

# Serialize (pickle) the instance to a file
with open("person.pkl", "wb") as file:
    pickle.dump(person, file)

# Deserialize (unpickle) the instance from the file
with open("person.pkl", "rb") as file:
    loaded_person = pickle.load(file)

print(loaded_person.greet())  # Output: Hello, my name is Alice and I am 30 years old.

'''
Q: What is the purpose of the `pickle` module in Python?
A: The `pickle` module in Python is used for serializing and deserializing Python objects. 
Serialization (or "pickling") is the process of converting a Python object into a byte stream, 
which can then be saved to a file or transmitted over a network. Deserialization (or "unpickling") is 
the reverse process, where the byte stream is converted back into a Python object. This allows for 
easy storage and retrieval of complex data structures, such as custom classes and objects.

Q: What are some potential security concerns when using the `pickle` module?
A: The `pickle` module can execute arbitrary code during the unpickling process, which poses a
security risk if the source of the pickled data is untrusted. An attacker could craft a 
malicious pickle file that, when unpickled, executes harmful code on the system. Therefore, it 
is important to only unpickle data from trusted sources and to consider alternative serialization
methods (such as JSON) for data that comes from untrusted sources.

Q: What are memory considerations when using the `pickle` module for large objects?
A: When using the `pickle` module for large objects, memory considerations include the fact that
pickling and unpickling large objects can consume significant amounts of memory, potentially leading
to memory issues or even out-of-memory errors.

Q: What are some alternatives to the `pickle` module for serialization in Python?
A: Some alternatives to the `pickle` module for serialization in Python include:
- JSON (JavaScript Object Notation): A lightweight data interchange format that is easy to read and 
write for humans and machines. It is widely used for web APIs and data exchange.
- YAML (YAML Ain't Markup Language): A human-readable data serialization format that is often used
for configuration files and data exchange between languages with different data structures.

'''
