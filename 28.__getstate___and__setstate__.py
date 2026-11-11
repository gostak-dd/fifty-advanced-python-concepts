import pickle

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "w")

    def write(self, data):
        self.file.write(data)

    def __getstate__(self):
        state = self.__dict__.copy()
        # Remove the non-pickleable file object
        del state["file"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        # Restore the file object
        self.file = open(self.filename, "w")

# Create an instance
handler = FileHandler("example.txt")
handler.write("Hello, World!")

# Serialize and deserialize the instance
with open("handler.pkl", "wb") as file:
    pickle.dump(handler, file)

with open("handler.pkl", "rb") as file:
    loaded_handler = pickle.load(file)

loaded_handler.write("Another line!")

'''
Q: What is the purpose of the `__getstate__` and `__setstate__` methods in the `FileHandler` class?
A: The `__getstate__` and `__setstate__` methods in the `FileHandler` class are used to 
customize the pickling and unpickling process for instances of the class. 
The `__getstate__` method is called when an instance is being pickled, and it returns a
dictionary representing the state of the object. In this case, it removes the non-pickleable
file object from the state before returning it. 
The `__setstate__` method is called when an instance is being unpickled, and it restores the state of 
the object from the provided dictionary.In this case, it reopens the file object using the filename 
stored in the state.

Q: Explain the flow of serialization and deserialization in the provided code snippet.
A: In the provided code snippet, the flow of serialization and deserialization is as follows:
1. An instance of the `FileHandler` class is created, which opens a file for writing.
2. The `write` method is called to write data to the file.
3. The instance is serialized (pickled) using the `pickle.dump` function, which calls the 
   `__getstate__` method to obtain the state of the object without the non-pickleable file object.
4. The serialized data is saved to a file named "handler.pkl".
5. The instance is deserialized (unpickled) using the `pickle.load` function,
which calls the `__setstate__` method to restore the state of the object and reopen the file for writing.
'''
