# =============================================================================
# Lesson 1.1: Lists, Dicts, Tuples
# =============================================================================
# In Laravel, you use arrays for everything. Python has 3 main types:
# - Lists   → Like PHP indexed arrays (mutable, ordered)
# - Dicts   → Like PHP associative arrays (key-value pairs)
# - Tuples  → Like arrays but IMMUTABLE (can't change after creation)
# =============================================================================

# -----------------------------------------------------------------------------
# LISTS - Like PHP indexed arrays
# -----------------------------------------------------------------------------
# PHP:  $users = ['Alice', 'Bob', 'Charlie'];
# Python:
users = ['Alice', 'Bob', 'Charlie']

# Accessing elements (same as PHP - zero indexed)
print(users[0])        # Alice
print(users[-1])       # Charlie (negative index = from end, PHP doesn't have this!)

# Adding elements
# PHP:  $users[] = 'David';  OR  array_push($users, 'David');
users.append('David')
print(users)           # ['Alice', 'Bob', 'Charlie', 'David']

# Slicing (PHP: array_slice)
# Python slicing is POWERFUL - syntax: list[start:end:step]
print(users[1:3])      # ['Bob', 'Charlie'] - items at index 1 and 2
print(users[:2])       # ['Alice', 'Bob'] - first 2 items
print(users[2:])       # ['Charlie', 'David'] - from index 2 to end

# Length
# PHP:  count($users)
print(len(users))      # 4


# -----------------------------------------------------------------------------
# DICTS - Like PHP associative arrays
# -----------------------------------------------------------------------------
# PHP:  $user = ['name' => 'Alice', 'age' => 30, 'role' => 'admin'];
# Python:
user = {'name': 'Alice', 'age': 30, 'role': 'admin'}

# Accessing values
# PHP:  $user['name']
print(user['name'])    # Alice

# Safe access (like $user['email'] ?? 'default' in PHP)
# PHP:  $user['email'] ?? 'no email'
print(user.get('email', 'no email'))  # no email

# Adding/updating
user['email'] = 'alice@example.com'
user['age'] = 31       # Update existing

# Looping through dict
# PHP:  foreach($user as $key => $value)
for key, value in user.items():
    print(f"{key}: {value}")

# Get all keys or values
print(user.keys())     # dict_keys(['name', 'age', 'role', 'email'])
print(user.values())   # dict_values(['Alice', 31, 'admin', 'alice@example.com'])


# -----------------------------------------------------------------------------
# TUPLES - Immutable lists (PHP has no equivalent)
# -----------------------------------------------------------------------------
# Use tuples when data shouldn't change (coordinates, RGB colors, etc.)
coordinates = (10, 20)
rgb_red = (255, 0, 0)

# Access like lists
print(coordinates[0])  # 10

# But you CAN'T modify them:
# coordinates[0] = 15  # This would raise an ERROR!

# Why use tuples?
# 1. Safer - prevents accidental modification
# 2. Faster - Python optimizes immutable data
# 3. Can be used as dict keys (lists can't)

# Tuple unpacking - very Pythonic!
x, y = coordinates
print(f"x={x}, y={y}")  # x=10, y=20

# This is how functions return multiple values in Python:
def get_user_info():
    return 'Alice', 30, 'admin'  # Returns a tuple

name, age, role = get_user_info()
print(f"{name} is {age} years old")


# -----------------------------------------------------------------------------
# QUICK COMPARISON
# -----------------------------------------------------------------------------
"""
| Feature          | PHP                    | Python               |
|------------------|------------------------|----------------------|
| Indexed array    | $arr = [1, 2, 3]       | arr = [1, 2, 3]      |
| Assoc array      | $arr = ['a' => 1]      | arr = {'a': 1}       |
| Access           | $arr[0] or $arr['key'] | arr[0] or arr['key'] |
| Add to list      | $arr[] = 4             | arr.append(4)        |
| Length           | count($arr)            | len(arr)             |
| Check key exists | isset($arr['key'])     | 'key' in arr         |
| Merge arrays     | array_merge($a, $b)    | [*a, *b] or {**a,**b}|
| Last element     | end($arr)              | arr[-1]              |
"""


# =============================================================================
# EXERCISE: Try these yourself!
# =============================================================================
# 1. Create a list of 5 programming languages you know
# 2. Create a dict representing a Laravel project (name, version, packages)
# 3. Use tuple unpacking to swap two variables: a, b = b, a

# Uncomment and complete:
# languages = [...]
# laravel_project = {...}
# a, b = 5, 10
# a, b = ...  # Swap them
# print(f"After swap: a={a}, b={b}")
