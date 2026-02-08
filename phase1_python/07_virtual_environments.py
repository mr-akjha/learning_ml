# =============================================================================
# Lesson 1.7: Virtual Environments & Package Management
# =============================================================================
# You know Composer in Laravel. Python has a similar but slightly different
# approach. This lesson is more about understanding concepts and terminal
# commands than writing code. But it's CRITICAL for ML work.
# =============================================================================


# -----------------------------------------------------------------------------
# WHY VIRTUAL ENVIRONMENTS?
# -----------------------------------------------------------------------------
# The Problem (same as Composer, but worse):
#
# In PHP/Laravel:
#   - Each project has its own vendor/ folder
#   - composer.json tracks dependencies per project
#   - Projects are isolated by default. Easy!
#
# In Python:
#   - By default, packages install GLOBALLY (like npm without node_modules)
#   - Project A needs numpy 1.24, Project B needs numpy 1.26 → CONFLICT!
#   - Virtual environments solve this by creating isolated Python per project
#
# Think of it as: each project gets its own vendor/ equivalent


# -----------------------------------------------------------------------------
# CREATING A VIRTUAL ENVIRONMENT
# -----------------------------------------------------------------------------
# Terminal commands (NOT Python code):
#
# Step 1: Create a virtual environment (do this once per project)
#   python3 -m venv venv
#
# This creates a 'venv/' folder (like vendor/ in Laravel)
# Convention is to name it 'venv' or '.venv'
#
# Step 2: Activate it
#   Mac/Linux: source venv/bin/activate
#   Windows:   venv\Scripts\activate
#
# Your terminal prompt will change to show (venv) at the start
# This means you're now "inside" the virtual environment
#
# Step 3: Deactivate when done
#   deactivate


# -----------------------------------------------------------------------------
# PIP - Python's Package Manager (Like Composer)
# -----------------------------------------------------------------------------
# Composer equivalents:
#
# | Composer                    | pip                            |
# |-----------------------------|--------------------------------|
# | composer require package    | pip install package            |
# | composer remove package     | pip uninstall package          |
# | composer install            | pip install -r requirements.txt|
# | composer.json               | requirements.txt               |
# | composer.lock               | requirements.txt (with ==)     |
# | vendor/                     | venv/lib/                      |
# | composer show               | pip list                       |
#
# Common commands:
#   pip install numpy              # Install a package
#   pip install numpy==1.24.0      # Install specific version
#   pip install numpy>=1.24        # Install minimum version
#   pip install -r requirements.txt # Install from file (like composer install)
#   pip list                        # Show installed packages
#   pip freeze > requirements.txt   # Save current packages to file


# -----------------------------------------------------------------------------
# requirements.txt - Like composer.json
# -----------------------------------------------------------------------------
# Your project already has one! It looks like:
#
#   numpy==1.24.0
#   pandas==2.0.0
#   scikit-learn==1.3.0
#   matplotlib==3.7.0
#
# The == means exact version (like "^1.24" in composer.json)
#
# Best practice:
#   pip freeze > requirements.txt    # Generate from current environment
#   pip install -r requirements.txt  # Install from file


# -----------------------------------------------------------------------------
# PROJECT SETUP WORKFLOW (What you'll do for every new project)
# -----------------------------------------------------------------------------
# This is like running: composer create-project laravel/laravel my-project
#
# 1. Create project folder:
#    mkdir my_ml_project && cd my_ml_project
#
# 2. Create virtual environment:
#    python3 -m venv venv
#
# 3. Activate it:
#    source venv/bin/activate    (Mac/Linux)
#
# 4. Install packages:
#    pip install numpy pandas scikit-learn matplotlib
#
# 5. Save dependencies:
#    pip freeze > requirements.txt
#
# 6. Add venv to .gitignore (like vendor/ in Laravel):
#    echo "venv/" >> .gitignore


# -----------------------------------------------------------------------------
# .gitignore FOR PYTHON - Like Laravel's .gitignore
# -----------------------------------------------------------------------------
# What to ignore (you already have a .gitignore, but good to know):
#
#   venv/                 # Virtual environment (like vendor/)
#   __pycache__/          # Python bytecode cache (like .phpunit.cache)
#   *.pyc                 # Compiled Python files
#   .env                  # Environment variables (same as Laravel!)
#   *.csv                 # Large data files
#   *.pkl                 # Saved ML models
#   .ipynb_checkpoints/   # Jupyter notebook checkpoints


# -----------------------------------------------------------------------------
# CHECKING YOUR SETUP
# -----------------------------------------------------------------------------
# Run these in your terminal to verify everything works:

import sys

# Which Python am I using? (Should point to your venv)
print(f"Python location: {sys.executable}")
print(f"Python version: {sys.version}")

# What's installed?
# In terminal: pip list
# In Python:
import importlib

packages_to_check = ['numpy', 'pandas', 'sklearn', 'matplotlib', 'json', 'csv', 'os']

print("\nPackage check:")
for package in packages_to_check:
    try:
        mod = importlib.import_module(package)
        version = getattr(mod, '__version__', 'built-in')
        print(f"  {package}: {version}")
    except ImportError:
        print(f"  {package}: NOT INSTALLED")


# -----------------------------------------------------------------------------
# COMMON GOTCHAS
# -----------------------------------------------------------------------------
"""
1. "ModuleNotFoundError: No module named 'numpy'"
   → You forgot to activate your venv, or forgot to pip install

2. "pip: command not found"
   → Try pip3 instead, or activate your venv first

3. "Permission denied" when installing
   → NEVER use sudo pip install! Use a virtual environment instead

4. Different Python versions
   → python vs python3 — on Mac, use python3
   → Inside venv, 'python' always works

5. Installing in wrong environment
   → Always check: which python (Mac) or where python (Windows)
   → Should point to your venv, not system Python
"""


# -----------------------------------------------------------------------------
# BEYOND PIP: OTHER TOOLS YOU MIGHT SEE
# -----------------------------------------------------------------------------
"""
| Tool      | What It Is                      | Like In PHP/JS         |
|-----------|---------------------------------|------------------------|
| pip       | Package installer (default)     | Composer               |
| venv      | Virtual environment (built-in)  | (built into Composer)  |
| conda     | Package + env manager (for ML)  | nvm + npm combined     |
| poetry    | Modern dependency management    | Composer (closer match)|
| pipenv    | pip + venv combined             | Composer               |

For now, pip + venv is all you need. You might switch to conda later
for ML-specific needs (it handles non-Python dependencies better).
"""


# -----------------------------------------------------------------------------
# QUICK REFERENCE CARD
# -----------------------------------------------------------------------------
"""
=== DAILY WORKFLOW ===
1. cd my_project
2. source venv/bin/activate      # Start working
3. python my_script.py           # Run code
4. pip install new_package       # Add dependency
5. pip freeze > requirements.txt # Save dependency
6. deactivate                    # Stop working

=== SETUP NEW PROJECT ===
1. mkdir project && cd project
2. python3 -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. echo "venv/" >> .gitignore
"""


# =============================================================================
# EXERCISE: Try these in your terminal!
# =============================================================================
# 1. Check if your virtual environment is activated:
#    which python    (should show .../venv/bin/python)
#
# 2. List all installed packages:
#    pip list
#
# 3. Install a fun package and try it:
#    pip install cowsay
#    python -c "import cowsay; cowsay.cow('Hello from Python!')"
#
# 4. Check your requirements.txt matches what's installed:
#    pip freeze
#    cat requirements.txt
#
# 5. Practice the full workflow:
#    mkdir /tmp/test_project && cd /tmp/test_project
#    python3 -m venv venv
#    source venv/bin/activate
#    pip install requests
#    pip freeze > requirements.txt
#    cat requirements.txt
#    deactivate
