# =============================================================================
# Lesson 1.5: File I/O & JSON
# =============================================================================
# In Laravel, you use Storage::get(), Storage::put(), json_decode/encode.
# Python has built-in file handling that's simpler — no facade needed.
# This is important for ML because you'll load datasets from files constantly.
# =============================================================================


# -----------------------------------------------------------------------------
# READING FILES - Like Storage::get()
# -----------------------------------------------------------------------------
# PHP/Laravel:
#   $content = Storage::get('file.txt');
#   $content = file_get_contents('file.txt');
#
# Python uses the 'with' statement (auto-closes the file for you):

# First, let's create a file to work with
# PHP: Storage::put('sample.txt', $content)
with open('sample.txt', 'w') as f:
    f.write("Line 1: Hello Python\n")
    f.write("Line 2: Coming from Laravel\n")
    f.write("Line 3: Learning ML\n")

# Now read it back
# 'r' = read mode (default)
with open('sample.txt', 'r') as f:
    content = f.read()     # Reads entire file as one string
    print(content)

# Why 'with'? It's like a try/finally that auto-closes the file.
# Think of it like Laravel's DB::transaction() — ensures cleanup happens.


# -----------------------------------------------------------------------------
# READING LINE BY LINE - Useful for large files
# -----------------------------------------------------------------------------
# PHP: You'd use fgets() in a loop
# Python:
print("--- Line by line ---")
with open('sample.txt', 'r') as f:
    for line in f:                  # Python files are iterable!
        print(line.strip())         # .strip() removes the trailing \n

# Or get all lines as a list
with open('sample.txt', 'r') as f:
    lines = f.readlines()          # Returns list of strings
    print(lines)                   # ['Line 1: Hello Python\n', ...]


# -----------------------------------------------------------------------------
# WRITING FILES - Like Storage::put()
# -----------------------------------------------------------------------------
# 'w' = write mode (creates or OVERWRITES)
# 'a' = append mode (adds to end)
# 'x' = create mode (fails if file exists)

# Write a new file
with open('output.txt', 'w') as f:
    f.write("This is line 1\n")
    f.write("This is line 2\n")

# Append to the file
with open('output.txt', 'a') as f:
    f.write("This was appended\n")

# Write multiple lines at once
lines_to_write = ['Apple\n', 'Banana\n', 'Cherry\n']
with open('fruits.txt', 'w') as f:
    f.writelines(lines_to_write)


# -----------------------------------------------------------------------------
# WORKING WITH JSON - Like json_encode/json_decode
# -----------------------------------------------------------------------------
import json

# PHP: $data = ['name' => 'Abhishek', 'skills' => ['PHP', 'Python']];
data = {
    'name': 'Abhishek',
    'age': 30,
    'skills': ['PHP', 'Laravel', 'Python'],
    'experience': {
        'backend': 7,
        'ml': 0
    }
}

# PHP: $json = json_encode($data, JSON_PRETTY_PRINT);
json_string = json.dumps(data, indent=2)  # dumps = dump to string
print(json_string)

# PHP: $decoded = json_decode($json, true);  // true for assoc array
decoded = json.loads(json_string)           # loads = load from string
print(decoded['name'])     # Abhishek
print(decoded['skills'])   # ['PHP', 'Laravel', 'Python']


# -----------------------------------------------------------------------------
# SAVING/LOADING JSON FILES - Like Storage::put with json_encode
# -----------------------------------------------------------------------------
# Save dict to JSON file
# PHP: Storage::put('data.json', json_encode($data, JSON_PRETTY_PRINT));
with open('user_data.json', 'w') as f:
    json.dump(data, f, indent=2)       # dump (no 's') writes to file

# Load JSON from file
# PHP: $data = json_decode(Storage::get('data.json'), true);
with open('user_data.json', 'r') as f:
    loaded_data = json.load(f)          # load (no 's') reads from file

print(loaded_data['experience'])       # {'backend': 7, 'ml': 0}


# -----------------------------------------------------------------------------
# WORKING WITH CSV FILES - Very common in ML!
# -----------------------------------------------------------------------------
import csv

# Writing CSV
# PHP: fputcsv($handle, $fields)
students = [
    ['Name', 'Age', 'Grade'],          # Header row
    ['Alice', 20, 'A'],
    ['Bob', 22, 'B'],
    ['Charlie', 21, 'A'],
]

with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(students)         # Write all rows at once

# Reading CSV
with open('students.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)              # Get first row (header)
    print(f"Columns: {header}")

    for row in reader:                 # Remaining rows
        print(f"  {row[0]} is {row[1]} years old, grade {row[2]}")

# Reading CSV as dicts (like reading JSON objects)
# Each row becomes a dict with header keys
with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['Name']}: Grade {row['Grade']}")


# -----------------------------------------------------------------------------
# PATH HANDLING - Like Laravel's storage_path(), base_path()
# -----------------------------------------------------------------------------
import os

# Get current directory (like base_path())
current_dir = os.getcwd()
print(f"Current dir: {current_dir}")

# Join paths safely (handles / vs \ on different OS)
# PHP: storage_path('app/data/file.csv')
file_path = os.path.join(current_dir, 'data', 'file.csv')
print(f"Full path: {file_path}")

# Check if file/directory exists
# PHP: Storage::exists('file.txt')
print(os.path.exists('sample.txt'))    # True
print(os.path.isfile('sample.txt'))    # True
print(os.path.isdir('data'))           # True if 'data' directory exists

# List files in directory (like Storage::files())
# PHP: Storage::files('app/data')
files = os.listdir('.')               # List current directory
print(f"Files here: {files}")


# -----------------------------------------------------------------------------
# CLEANUP - Remove the files we created (optional)
# -----------------------------------------------------------------------------
# Uncomment these to clean up:
# os.remove('sample.txt')
# os.remove('output.txt')
# os.remove('fruits.txt')
# os.remove('user_data.json')
# os.remove('students.csv')


# -----------------------------------------------------------------------------
# QUICK REFERENCE
# -----------------------------------------------------------------------------
"""
| PHP/Laravel                         | Python                           |
|-------------------------------------|----------------------------------|
| file_get_contents('f.txt')          | open('f.txt').read()             |
| Storage::put('f.txt', $data)        | open('f.txt','w').write(data)    |
| json_encode($data)                  | json.dumps(data)                 |
| json_decode($json, true)            | json.loads(json_str)             |
| storage_path('file.csv')            | os.path.join(dir, 'file.csv')    |
| Storage::exists('file')             | os.path.exists('file')           |
| fputcsv / fgetcsv                   | csv.writer / csv.reader          |
"""


# =============================================================================
# EXERCISE: Try these yourself!
# =============================================================================
# 1. Create a JSON file called 'config.json' with:
#    - app_name, version, debug (bool), allowed_hosts (list)
#    Then read it back and print each setting.

# 2. Create a CSV file of 5 products (name, price, category)
#    Then read it and print only products over ₹100

# 3. Write a function that takes a filename and returns the number of
#    lines, words, and characters (like the 'wc' command)
# def file_stats(filename):
#     ...
