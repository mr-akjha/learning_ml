# =============================================================================
# Lesson 1.3: Functions & *args/**kwargs
# =============================================================================
# Functions in Python are similar to PHP, but with some powerful extras.
# Python's *args and **kwargs are like PHP's variadic functions on steroids.
# =============================================================================


# -----------------------------------------------------------------------------
# BASIC FUNCTIONS
# -----------------------------------------------------------------------------
# PHP:
#   function greet($name) {
#       return "Hello, $name!";
#   }
#
# Python:
def greet(name):
    return f"Hello, {name}!"

print(greet('Abhishek'))   # Hello, Abhishek!

# Key difference: Python uses indentation (not curly braces) to define blocks.
# This is non-negotiable — wrong indentation = error!


# -----------------------------------------------------------------------------
# DEFAULT PARAMETERS - Same concept as PHP
# -----------------------------------------------------------------------------
# PHP:  function greet($name, $greeting = 'Hello') { ... }
# Python:
def greet_with(name, greeting='Hello'):
    return f"{greeting}, {name}!"

print(greet_with('Abhishek'))              # Hello, Abhishek!
print(greet_with('Abhishek', 'Namaste'))   # Namaste, Abhishek!


# -----------------------------------------------------------------------------
# KEYWORD ARGUMENTS - PHP doesn't have this (until PHP 8 named arguments)
# -----------------------------------------------------------------------------
# In Python, you can pass arguments by name in any order:
def create_user(name, age, role='viewer'):
    return {'name': name, 'age': age, 'role': role}

# All of these work:
user1 = create_user('Alice', 30)                    # positional
user2 = create_user(name='Bob', age=25)              # keyword
user3 = create_user(age=35, name='Charlie')          # any order!
user4 = create_user('David', role='admin', age=28)   # mixed

print(user3)  # {'name': 'Charlie', 'age': 35, 'role': 'viewer'}

# This is like PHP 8's named arguments:
#   create_user(age: 35, name: 'Charlie')


# -----------------------------------------------------------------------------
# MULTIPLE RETURN VALUES - PHP can't do this easily
# -----------------------------------------------------------------------------
# PHP: You'd return an array or use list() = ...
# Python: Just return multiple values (it's a tuple under the hood)
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9


# -----------------------------------------------------------------------------
# *args - VARIABLE POSITIONAL ARGUMENTS
# -----------------------------------------------------------------------------
# PHP:  function sum_all(int ...$numbers) { return array_sum($numbers); }
# Python:
def sum_all(*args):
    """args becomes a tuple of all positional arguments passed."""
    print(f"Received: {args}")   # Shows the tuple
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))       # Received: (1, 2, 3) → 6
print(sum_all(10, 20, 30, 40)) # Received: (10, 20, 30, 40) → 100

# You can also use built-in sum():
def sum_all_v2(*args):
    return sum(args)


# -----------------------------------------------------------------------------
# **kwargs - VARIABLE KEYWORD ARGUMENTS
# -----------------------------------------------------------------------------
# PHP has no direct equivalent. Closest is passing an associative array.
# PHP:  function create($data) { ... } → create(['name' => 'Alice', 'age' => 30])
# Python:
def create_profile(**kwargs):
    """kwargs becomes a dict of all keyword arguments passed."""
    print(f"Received: {kwargs}")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

create_profile(name='Alice', age=30, city='Mumbai')
# Received: {'name': 'Alice', 'age': 30, 'city': 'Mumbai'}
#   name = Alice
#   age = 30
#   city = Mumbai


# -----------------------------------------------------------------------------
# COMBINING *args AND **kwargs
# -----------------------------------------------------------------------------
# This is used a LOT in Python libraries and frameworks
def flexible_function(required_arg, *args, **kwargs):
    print(f"Required: {required_arg}")
    print(f"Extra positional: {args}")
    print(f"Extra keyword: {kwargs}")

flexible_function('hello', 1, 2, 3, debug=True, verbose=False)
# Required: hello
# Extra positional: (1, 2, 3)
# Extra keyword: {'debug': True, 'verbose': False}

# Real-world example: a logging function
def log(message, *tags, **metadata):
    tag_str = ', '.join(tags) if tags else 'none'
    print(f"[{tag_str}] {message}")
    for key, value in metadata.items():
        print(f"  {key}: {value}")

log('User logged in', 'auth', 'security', user_id=42, ip='127.0.0.1')


# -----------------------------------------------------------------------------
# UNPACKING LISTS/DICTS INTO FUNCTION CALLS
# -----------------------------------------------------------------------------
# This is the reverse — passing a list/dict AS arguments
# PHP:  No direct equivalent (you'd use call_user_func_array)

def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))       # Unpacks list → add(1, 2, 3) = 6

config = {'a': 10, 'b': 20, 'c': 30}
print(add(**config))       # Unpacks dict → add(a=10, b=20, c=30) = 60


# -----------------------------------------------------------------------------
# LAMBDA FUNCTIONS - Like PHP arrow functions
# -----------------------------------------------------------------------------
# PHP:  $double = fn($x) => $x * 2;
# Python:
double = lambda x: x * 2
print(double(5))           # 10

# Lambdas are most useful with functions like sorted(), map(), filter()
users = [
    {'name': 'Charlie', 'age': 35},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
]

# Sort by age (like ->sortBy('age'))
sorted_users = sorted(users, key=lambda u: u['age'])
print([u['name'] for u in sorted_users])  # ['Bob', 'Alice', 'Charlie']

# Sort by name
sorted_by_name = sorted(users, key=lambda u: u['name'])
print([u['name'] for u in sorted_by_name])  # ['Alice', 'Bob', 'Charlie']


# -----------------------------------------------------------------------------
# TYPE HINTS - Like PHP type declarations
# -----------------------------------------------------------------------------
# PHP:  function add(int $a, int $b): int { return $a + $b; }
# Python:
def add_typed(a: int, b: int) -> int:
    return a + b

# Type hints are OPTIONAL and not enforced at runtime (unlike PHP's strict mode)
# They're for documentation and IDE support
# You'll see them heavily in ML libraries


# -----------------------------------------------------------------------------
# QUICK REFERENCE
# -----------------------------------------------------------------------------
"""
| PHP                              | Python                          |
|----------------------------------|---------------------------------|
| function name($a) {}             | def name(a):                    |
| function($a) => $a * 2           | lambda a: a * 2                 |
| function sum(...$nums) {}        | def sum(*args):                 |
| function create($data = []) {}   | def create(**kwargs):           |
| return [$a, $b]                  | return a, b                     |
| function add(int $a): int {}     | def add(a: int) -> int:         |
"""


# =============================================================================
# EXERCISE: Try these yourself!
# =============================================================================
# 1. Write a function that takes any number of strings and returns them
#    joined with " | " (like implode in PHP)
# def join_strings(*args):
#     ...

# 2. Write a function that takes a name and any number of keyword arguments
#    and prints a profile card
# def profile_card(name, **details):
#     ...
# profile_card('Abhishek', language='Python', experience='7 years')

# 3. Write a function that returns both the sum and average of a list
# def stats(numbers):
#     ...
# total, avg = stats([10, 20, 30, 40, 50])

# 4. Sort this list of tuples by the second element using a lambda:
# pairs = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]
# sorted_pairs = sorted(pairs, key=...)
