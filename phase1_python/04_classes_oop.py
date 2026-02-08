# =============================================================================
# Lesson 1.4: Classes & OOP
# =============================================================================
# You already know OOP from Laravel — Models, Services, Controllers.
# Python OOP is simpler (less boilerplate) but follows the same principles.
# Think of Python classes like Laravel Models but more lightweight.
# =============================================================================


# -----------------------------------------------------------------------------
# BASIC CLASS - Like a Laravel Model
# -----------------------------------------------------------------------------
# PHP/Laravel:
#   class User extends Model {
#       protected $fillable = ['name', 'email'];
#       public function __construct($name, $email) { ... }
#   }
#
# Python:
class User:
    # __init__ is like PHP's __construct
    def __init__(self, name, email):
        self.name = name       # Like $this->name = $name
        self.email = email     # Like $this->email = $email

    # Methods always take 'self' as first parameter (like $this in PHP)
    def greet(self):
        return f"Hi, I'm {self.name} ({self.email})"

# Creating instances (no 'new' keyword needed!)
# PHP: $user = new User('Alice', 'alice@example.com');
user = User('Alice', 'alice@example.com')
print(user.greet())        # Hi, I'm Alice (alice@example.com)
print(user.name)           # Alice (attributes are public by default)


# -----------------------------------------------------------------------------
# __str__ AND __repr__ - Like PHP's __toString()
# -----------------------------------------------------------------------------
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # __str__ is what print() uses (like __toString in PHP)
    def __str__(self):
        return f"{self.name} - ₹{self.price}"

    # __repr__ is for debugging (shows how to recreate the object)
    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

product = Product('Laptop', 75000)
print(product)             # Laptop - ₹75000 (uses __str__)
print(repr(product))       # Product('Laptop', 75000) (uses __repr__)


# -----------------------------------------------------------------------------
# INSTANCE vs CLASS ATTRIBUTES
# -----------------------------------------------------------------------------
class Counter:
    # Class attribute - shared by ALL instances (like static in PHP)
    total_count = 0

    def __init__(self, name):
        self.name = name       # Instance attribute - unique to each instance
        self.count = 0
        Counter.total_count += 1

    def increment(self):
        self.count += 1

c1 = Counter('page_views')
c2 = Counter('clicks')
c1.increment()
c1.increment()
c2.increment()
print(f"{c1.name}: {c1.count}")           # page_views: 2
print(f"{c2.name}: {c2.count}")           # clicks: 1
print(f"Total counters: {Counter.total_count}")  # Total counters: 2


# -----------------------------------------------------------------------------
# INHERITANCE - Like extends in PHP/Laravel
# -----------------------------------------------------------------------------
# PHP:
#   class Admin extends User {
#       public function __construct($name, $email, $level) {
#           parent::__construct($name, $email);
#           $this->level = $level;
#       }
#   }
#
# Python:
class Admin(User):  # Admin inherits from User
    def __init__(self, name, email, level):
        super().__init__(name, email)  # Like parent::__construct()
        self.level = level

    # Override parent method
    def greet(self):
        return f"Hi, I'm {self.name} (Admin Level {self.level})"

admin = Admin('Bob', 'bob@example.com', 5)
print(admin.greet())       # Hi, I'm Bob (Admin Level 5)
print(admin.email)         # bob@example.com (inherited from User)

# Check inheritance
print(isinstance(admin, Admin))  # True
print(isinstance(admin, User))   # True (Admin IS a User)


# -----------------------------------------------------------------------------
# ENCAPSULATION - Private/Protected attributes
# -----------------------------------------------------------------------------
# PHP: private $password; protected $role;
# Python: Uses naming conventions (not enforced like PHP)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._bank_name = 'SBI'     # "Protected" (convention: single underscore)
        self.__balance = balance    # "Private" (name mangling: double underscore)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount('Abhishek', 1000)
print(account.owner)              # Works fine
print(account._bank_name)         # Works but signals "don't touch this"
# print(account.__balance)        # AttributeError! (name mangled)
print(account.get_balance())      # 1000 (use the getter)


# -----------------------------------------------------------------------------
# PROPERTIES - Like Laravel Accessors/Mutators
# -----------------------------------------------------------------------------
# PHP/Laravel:
#   public function getFullNameAttribute() { return "{$this->first} {$this->last}"; }
#   public function setEmailAttribute($value) { $this->attributes['email'] = strtolower($value); }
#
# Python uses @property decorator:
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self._salary = salary

    # Getter (like Laravel accessor)
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Getter for salary
    @property
    def salary(self):
        return self._salary

    # Setter with validation (like Laravel mutator)
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value

emp = Employee('Abhishek', 'Kumar', 50000)
print(emp.full_name)       # Abhishek Kumar (looks like an attribute, but it's a method!)
emp.salary = 60000         # Uses the setter
print(emp.salary)          # 60000
# emp.salary = -100        # Raises ValueError!


# -----------------------------------------------------------------------------
# DUNDER (MAGIC) METHODS - Like PHP magic methods
# -----------------------------------------------------------------------------
# Python has special methods like __len__, __eq__, __add__ etc.
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item, price):
        self.items.append({'item': item, 'price': price})

    # len(cart) will use this
    def __len__(self):
        return len(self.items)

    # Makes the cart iterable in for loops
    def __iter__(self):
        return iter(self.items)

    # cart[0] will use this
    def __getitem__(self, index):
        return self.items[index]

    def __str__(self):
        total = sum(item['price'] for item in self.items)
        return f"Cart({len(self)} items, total: ₹{total})"

cart = ShoppingCart()
cart.add('Book', 299)
cart.add('Pen', 49)
cart.add('Notebook', 99)

print(len(cart))           # 3
print(cart[0])             # {'item': 'Book', 'price': 299}
print(cart)                # Cart(3 items, total: ₹447)

for item in cart:          # Works because of __iter__
    print(f"  {item['item']}: ₹{item['price']}")


# -----------------------------------------------------------------------------
# QUICK REFERENCE
# -----------------------------------------------------------------------------
"""
| PHP/Laravel                     | Python                          |
|---------------------------------|---------------------------------|
| class User { }                  | class User:                     |
| public function __construct()   | def __init__(self):             |
| $this->name                     | self.name                       |
| new User()                      | User()                          |
| class Admin extends User        | class Admin(User):              |
| parent::__construct()           | super().__init__()              |
| private $x                      | self.__x (name mangling)        |
| getXAttribute()                 | @property                       |
| __toString()                    | __str__()                       |
| instanceof                      | isinstance()                    |
"""


# =============================================================================
# EXERCISE: Try these yourself!
# =============================================================================
# 1. Create a 'Book' class with title, author, pages
#    - Add a __str__ method that prints nicely
#    - Add a property 'is_long' that returns True if pages > 300

# 2. Create an 'Ebook' class that inherits from Book
#    - Add a 'file_size' attribute (in MB)
#    - Override __str__ to include file size

# 3. Create a 'Library' class that stores books
#    - Add an 'add_book' method
#    - Make len(library) return number of books
#    - Add a 'search' method that finds books by title (partial match)
