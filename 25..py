## Run test_pytest_1.py for this file

import pytest

@pytest.mark.parametrize("user_id,expected_name", [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie"),
    (3, "Charlie"),
    (3, "Charlie"),
    (8, "Gary"),
])
def test_get_user_details(user_id, expected_name):
    # Simulating an API function
    def fetch_user_details(user_id):
        users = {1: "Alice", 2: "Bob", 3: "Charlie", 8: "Gary"}
        return {"id": user_id, "name": users.get(user_id, "Unknown")}
    
    response = fetch_user_details(user_id)
    assert response["name"] == expected_name


'''
Q: What is pytest?
A: pytest is a testing framework for Python that allows developers to write simple and scalable test cases

Q: How does the `@pytest.mark.parametrize` decorator work in the provided code?
A: The `@pytest.mark.parametrize` decorator allows you to define multiple sets of input parameters
for a single test function. In the provided code, it is used to run the `test_get_user_details` function 
multiple times with different `user_id` and `expected_name` values. 
Each tuple in the list represents a set of parameters for one test case, 
enabling efficient testing of various scenarios without writing separate test functions for each case.
'''
