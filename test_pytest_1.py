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
