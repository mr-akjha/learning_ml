# =============================================================================
# Lesson 1.6: Error Handling
# =============================================================================
# You know try-catch from PHP/Laravel. Python's try-except is almost identical.
# Good error handling is crucial in ML — bad data, missing files, wrong formats
# will happen ALL the time when working with datasets.
# =============================================================================


# -----------------------------------------------------------------------------
# BASIC TRY-EXCEPT - Like PHP's try-catch
# -----------------------------------------------------------------------------
# PHP:
#   try {
#       $result = 10 / 0;
#   } catch (DivisionByZeroError $e) {
#       echo "Can't divide by zero!";
#   }
#
# Python:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")


# -----------------------------------------------------------------------------
# CATCHING THE ERROR OBJECT - Like $e in PHP
# -----------------------------------------------------------------------------
# PHP: catch (Exception $e) { echo $e->getMessage(); }
# Python:
try:
    numbers = [1, 2, 3]
    print(numbers[10])     # Index doesn't exist
except IndexError as e:
    print(f"Error: {e}")   # Error: list index out of range


# -----------------------------------------------------------------------------
# MULTIPLE EXCEPT BLOCKS - Like multiple catch blocks
# -----------------------------------------------------------------------------
# PHP:
#   try { ... }
#   catch (TypeError $e) { ... }
#   catch (ValueError $e) { ... }
#
# Python:
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError as e:
        print(f"Wrong types: {e}")
        return None

print(divide(10, 2))      # 5.0
print(divide(10, 0))      # Cannot divide by zero! → None
print(divide("10", 2))    # Wrong types: ... → None


# -----------------------------------------------------------------------------
# CATCH MULTIPLE EXCEPTIONS IN ONE BLOCK
# -----------------------------------------------------------------------------
# PHP: catch (TypeError | ValueError $e) { ... }   (PHP 8+)
# Python:
try:
    value = int("not a number")
except (ValueError, TypeError) as e:
    print(f"Conversion error: {e}")


# -----------------------------------------------------------------------------
# ELSE AND FINALLY - PHP has finally too
# -----------------------------------------------------------------------------
# Python has an extra 'else' block that PHP doesn't have!
def read_file_safely(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        content = None
    else:
        # Runs ONLY if no exception occurred (PHP doesn't have this!)
        print(f"Successfully read {len(content)} characters")
    finally:
        # Always runs, just like PHP's finally
        print("Done attempting to read file")

    return content

read_file_safely('sample.txt')        # If file exists from lesson 1.5
read_file_safely('nonexistent.txt')   # File not found


# -----------------------------------------------------------------------------
# RAISING EXCEPTIONS - Like PHP's throw
# -----------------------------------------------------------------------------
# PHP: throw new InvalidArgumentException("Age must be positive");
# Python:
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age must be positive")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")   # Invalid age: Age must be positive


# -----------------------------------------------------------------------------
# CUSTOM EXCEPTIONS - Like custom Laravel exceptions
# -----------------------------------------------------------------------------
# PHP:
#   class InsufficientFundsException extends Exception { }
#
# Python:
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ₹{amount}. Balance is only ₹{balance}"
        )

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(1000)
try:
    account.withdraw(1500)
except InsufficientFundsError as e:
    print(f"Error: {e}")
    print(f"You tried: ₹{e.amount}, Available: ₹{e.balance}")


# -----------------------------------------------------------------------------
# COMMON PYTHON EXCEPTIONS YOU'LL SEE IN ML
# -----------------------------------------------------------------------------
"""
| Exception          | When It Happens                  | ML Context           |
|--------------------|----------------------------------|----------------------|
| FileNotFoundError  | File doesn't exist               | Dataset not found    |
| ValueError         | Wrong value type/format          | Bad data in CSV      |
| KeyError           | Dict key doesn't exist           | Missing column       |
| IndexError         | List index out of range          | Wrong array shape    |
| TypeError          | Wrong type for operation         | String vs number     |
| ImportError        | Module not installed             | Missing library      |
| ZeroDivisionError  | Division by zero                 | Empty dataset stats  |
| AttributeError     | Object doesn't have attribute    | Wrong method name    |
"""


# -----------------------------------------------------------------------------
# PRACTICAL PATTERN: SAFE DATA PROCESSING
# -----------------------------------------------------------------------------
# This is how you'd handle messy data (very common in ML)
def process_records(records):
    """Process a list of records, handling bad data gracefully."""
    results = []
    errors = []

    for i, record in enumerate(records):
        try:
            # Try to process each record
            name = record['name']
            age = int(record['age'])     # Could fail if age is "unknown"
            score = float(record['score'])  # Could fail too

            results.append({
                'name': name,
                'age': age,
                'score': score
            })
        except (KeyError, ValueError, TypeError) as e:
            # Log the error but keep processing other records
            errors.append(f"Record {i}: {e}")

    return results, errors

# Some messy data (typical of real-world datasets!)
records = [
    {'name': 'Alice', 'age': '30', 'score': '95.5'},
    {'name': 'Bob', 'age': 'twenty', 'score': '88.0'},    # Bad age!
    {'name': 'Charlie', 'age': '25'},                       # Missing score!
    {'name': 'David', 'age': '28', 'score': '92.3'},
]

good_data, bad_data = process_records(records)
print(f"\nProcessed {len(good_data)} records successfully")
print(f"Errors in {len(bad_data)} records:")
for error in bad_data:
    print(f"  {error}")


# -----------------------------------------------------------------------------
# QUICK REFERENCE
# -----------------------------------------------------------------------------
"""
| PHP                               | Python                            |
|-----------------------------------|-----------------------------------|
| try { }                           | try:                              |
| catch (Exception $e) { }         | except Exception as e:            |
| catch (A | B $e) { }             | except (A, B) as e:               |
| finally { }                       | finally:                          |
| throw new Exception("msg")        | raise Exception("msg")            |
| class MyError extends Exception   | class MyError(Exception):         |
| $e->getMessage()                  | str(e)                            |
| (no equivalent)                   | else: (runs if no exception)      |
"""


# =============================================================================
# EXERCISE: Try these yourself!
# =============================================================================
# 1. Write a function safe_divide(a, b) that:
#    - Returns a/b if possible
#    - Returns None and prints a message for ZeroDivisionError
#    - Returns None and prints a message for TypeError

# 2. Create a custom exception 'InvalidEmailError'
#    Write a validate_email(email) function that:
#    - Raises InvalidEmailError if email doesn't contain '@'
#    - Raises InvalidEmailError if email doesn't contain '.'
#    - Returns the email lowercased if valid

# 3. Write a function that reads a JSON file and returns the data.
#    Handle: FileNotFoundError, json.JSONDecodeError
#    Return an empty dict {} if anything goes wrong.
# import json
# def safe_json_load(filename):
#     ...
