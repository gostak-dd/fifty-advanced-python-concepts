from weakref import WeakKeyDictionary

class Widget:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Widget({self.name})"

# Create a WeakKeyDictionary for storing metadata
widget_metadata = WeakKeyDictionary()

# Create some widgets
widget1 = Widget("Button1")
widget2 = Widget("Button2")

# Attach metadata
widget_metadata[widget1] = {"color": "blue", "size": "small"}
widget_metadata[widget2] = {"color": "red", "size": "large"}

print(dict(widget_metadata))  # Output: {Widget(Button1): {...}, Widget(Button2): {...}}

# Remove a strong reference
del widget1

# The metadata for widget1 is automatically cleaned up
print(dict(widget_metadata))  # Output: {Widget(Button2): {...}}

'''
Q: What is the purpose of using a WeakKeyDictionary in this code?
A: The purpose of using a WeakKeyDictionary in this code is to store metadata associated with 
Widget instances without preventing those instances from being garbage collected. When a Widget 
instance (like widget1) is deleted or goes out of scope, its entry in the WeakKeyDictionary is 
automatically removed, ensuring that memory is managed efficiently and preventing memory leaks. 
This allows the program to maintain metadata for active widgets while allowing unused widgets to be 
cleaned up by the garbage collector.
'''
