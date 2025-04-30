# Basic Python Syntax Examples

# Variable declarations
x = 10
y = 5.5
name = "Data Analyst"

# List example
numbers = [1, 2, 3, 4, 5]

doubleNumber = [x*2 for x in numbers]

# Dictionary example
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

student = {
    "name": "Alice",
    "age": 22,
    "courses": ["Math", "Science"]
}

# Function to process a list
def process_list(lst):
    return [i * 2 for i in lst]

# Function to process a dictionary
def process_dict(d):
    return {key: str(value).upper() for key, value in d.items()}

def info_student(student):
    return {key: str(value).lower() for key, value in student.items()}

def find_max(lst):
    """Find the maximum value in a list."""
    if not lst:
        return None
    max_value = lst[0]
    for num in lst[1:]:
        if num > max_value:
            max_value = num
    return max_value

def find_min(lst):
    """Find the minimum value in a list."""
    if not lst:
        return None
    min_value = lst[0]
    for num in lst[1:]:
        if num < min_value:
            min_value = num
    return min_value


def filter_gioi(students):
    return [s for s in students if s["score"] >= 8.0]


# Example usage
if __name__ == "__main__":
    print("Variable x:", x)
    print("Variable y:", y)
    print("Name:", name)
    
    print("Processed List:", process_list(numbers))
    print("Processed Dictionary:", process_dict(person))
    print("Max of numbers:", find_max(numbers))
    print("Min of numbers:", find_min(numbers))
    print("Student Info:", info_student(student))

        # Test
    print("Hoc sinh gioi: " ,filter_gioi([
        {"name": "Lan", "score": 8.5},
        {"name": "Minh", "score": 7.0},
        {"name": "Hùng", "score": 6.5}
    ]))

    print(doubleNumber);