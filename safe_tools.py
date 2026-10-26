
def safe_divide(a, b):
    """Safely divide two numbers, handles ZeroDivisionError"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

def safe_convert_to_int(value):
    """Safely convert value to int, handles ValueError like 'abc'"""
    try:
        result = int(value)
        return result
    except ValueError:
        return f"Error: Cannot convert '{value}' to integer"

def safe_get_value(my_dict, key):
    """Safely get value from dict, handles KeyError"""
    try:
        result = my_dict[key]
        return result
    except KeyError:
        return f"Error: Key '{key}' not found"

# --- Main program to demonstrate ---
if __name__ == "__main__":
    print("1. Testing Division:")
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")

    print("\n2. Testing Conversion:")
    print(f"'123' -> {safe_convert_to_int('123')}")
    print(f"'abc' -> {safe_convert_to_int('abc')}")

    print("\n3. Testing Dictionary:")
    my_data = {"name": "Adam", "age": 22}
    print(f"Existing key 'name': {safe_get_value(my_data, 'name')}")
    print(f"Missing key 'city': {safe_get_value(my_data, 'city')}")
