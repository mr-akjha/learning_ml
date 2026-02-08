# =============================================================================
# Lesson 1.2: List Comprehensions
# =============================================================================
# In Laravel, you use Collection methods like ->map(), ->filter(), ->pluck().
# Python has a beautiful one-liner syntax called "list comprehensions" that
# does the same thing — and it's one of the most Pythonic features you'll use.
# =============================================================================


# -----------------------------------------------------------------------------
# BASIC LIST COMPREHENSION - Like Collection::map()
# -----------------------------------------------------------------------------
# PHP/Laravel:
#   $numbers = [1, 2, 3, 4, 5];
#   $doubled = collect($numbers)->map(fn($n) => $n * 2)->all();
#
# Python (the old way - using a loop):
numbers = [1, 2, 3, 4, 5]
doubled_loop = []
for n in numbers:
    doubled_loop.append(n * 2)
print(doubled_loop)        # [2, 4, 6, 8, 10]

# Python (the Pythonic way - list comprehension):
doubled = [n * 2 for n in numbers]
print(doubled)             # [2, 4, 6, 8, 10]

# Read it like English: "give me n*2 FOR each n IN numbers"
# Pattern: [expression FOR variable IN iterable]


# -----------------------------------------------------------------------------
# FILTERING - Like Collection::filter()
# -----------------------------------------------------------------------------
# PHP/Laravel:
#   $evens = collect($numbers)->filter(fn($n) => $n % 2 == 0)->values()->all();
#
# Python:
evens = [n for n in numbers if n % 2 == 0]
print(evens)               # [2, 4]

# Pattern: [expression FOR variable IN iterable IF condition]
# Read it: "give me n FOR each n IN numbers IF n is even"

# More examples:
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Get names longer than 3 characters (like ->filter())
long_names = [name for name in names if len(name) > 3]
print(long_names)          # ['Alice', 'Charlie', 'David']

# Uppercase all names (like ->map())
upper_names = [name.upper() for name in names]
print(upper_names)         # ['ALICE', 'BOB', 'CHARLIE', 'DAVID', 'EVE']


# -----------------------------------------------------------------------------
# MAP + FILTER COMBINED
# -----------------------------------------------------------------------------
# PHP/Laravel:
#   collect($names)->filter(fn($n) => strlen($n) > 3)->map(fn($n) => strtoupper($n));
#
# Python: filter AND transform in one line
long_upper = [name.upper() for name in names if len(name) > 3]
print(long_upper)          # ['ALICE', 'CHARLIE', 'DAVID']


# -----------------------------------------------------------------------------
# WORKING WITH DICTS - Like Collection::pluck()
# -----------------------------------------------------------------------------
users = [
    {'name': 'Alice', 'age': 30, 'active': True},
    {'name': 'Bob', 'age': 25, 'active': False},
    {'name': 'Charlie', 'age': 35, 'active': True},
]

# PHP/Laravel: collect($users)->pluck('name')->all()
names_list = [user['name'] for user in users]
print(names_list)          # ['Alice', 'Bob', 'Charlie']

# PHP/Laravel: collect($users)->where('active', true)->pluck('name')->all()
active_names = [user['name'] for user in users if user['active']]
print(active_names)        # ['Alice', 'Charlie']


# -----------------------------------------------------------------------------
# DICT COMPREHENSIONS - Building dicts on the fly
# -----------------------------------------------------------------------------
# PHP: No direct equivalent, you'd use array_combine or a loop
#
# Python: {key: value for item in iterable}
name_lengths = {name: len(name) for name in names}
print(name_lengths)        # {'Alice': 5, 'Bob': 3, 'Charlie': 7, ...}

# Create a lookup dict from a list of dicts (like ->keyBy())
# PHP/Laravel: collect($users)->keyBy('name')
users_by_name = {user['name']: user for user in users}
print(users_by_name['Alice'])  # {'name': 'Alice', 'age': 30, 'active': True}


# -----------------------------------------------------------------------------
# SET COMPREHENSIONS - Unique values only
# -----------------------------------------------------------------------------
# PHP: array_unique(array_map(fn($u) => $u['active'], $users))
ages = [25, 30, 25, 35, 30, 40]
unique_ages = {age for age in ages}  # Uses curly braces, no key:value
print(unique_ages)         # {25, 30, 35, 40} (order may vary)


# -----------------------------------------------------------------------------
# NESTED COMPREHENSIONS - Use sparingly!
# -----------------------------------------------------------------------------
# Flatten a 2D list (like Collection::flatten())
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)                # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Tip: If a comprehension gets hard to read, use a regular loop instead.
# Readability > cleverness!


# -----------------------------------------------------------------------------
# WHEN TO USE WHAT
# -----------------------------------------------------------------------------
"""
| Situation                    | Use This              |
|------------------------------|-----------------------|
| Transform each item          | [expr for x in list]  |
| Filter items                 | [x for x in list if ] |
| Transform + filter           | [expr for x if cond]  |
| Build a dict                 | {k: v for x in list}  |
| Unique values                | {x for x in list}     |
| Complex logic (many lines)   | Regular for loop      |
| Side effects (print, save)   | Regular for loop      |
"""


# =============================================================================
# EXERCISE: Try these yourself!
# =============================================================================
# Given this data:
products = [
    {'name': 'Laptop', 'price': 999, 'in_stock': True},
    {'name': 'Mouse', 'price': 29, 'in_stock': True},
    {'name': 'Keyboard', 'price': 79, 'in_stock': False},
    {'name': 'Monitor', 'price': 449, 'in_stock': True},
    {'name': 'Webcam', 'price': 69, 'in_stock': False},
]

# 1. Get a list of all product names
# product_names = [...]

# 2. Get names of products that are in stock
# in_stock_names = [...]

# 3. Get products over $50 that are in stock (list of dicts)
# expensive_available = [...]

# 4. Create a dict of {name: price} for all products
# price_lookup = {...}

# 5. Apply a 10% discount to all prices (list of new prices)
# discounted = [...]
