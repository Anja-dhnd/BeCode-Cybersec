#  Bad Practices when Coding in Python


## 0) Naming
### a) Meaningless, non-pertinent names. Bad:

k = "yellow"
a = False

tchtlkDt = "16/05/2022"

### Good Practice:

color = "yellow"
activate = False
techtalk_date = "16/05/2022"

### b) Overriding built-in names
### Bad:

id = 2
zip = 6000
list = [1, 2, 3]

### Good Practice:

id_number = 2
zip_code = 6000
number_list = ["1", "2", "3"]


### c) Using camelCase in names
### Bad:

def computeNetValue(price, tax):
    return price * (1 + tax)


### Good Practice (snake_case or PascalCase, PEP 8 style guide):

def compute_net_value(price, tax):
    return price * (1 + tax)


class MyClass:
    def __init__(self, name):
        self.name = name


## 1) Operators.
#
# a) ^ != exponentiation

y = 8 ^ 2  # bitwise XOR operator
x = 8 ** 2  # exponentiation

## 2) Modules/Libraries/Packages.
#
# a) Importing * from a module
### Bad:


from math import *  # imports all from math module

x = ceil(x)

### Good Practice:

from math import ceil

x = ceil(x)


## b) Installing modules the wrong way
# Bad:
# Systemwide installation of Python libraries is generally bad, you can make a mess of your system

# Good Practice:
### pip install <package> # installs a package in your local python environment
#
### virtualenv - create isolated python envs for your projects
# python3 -m venv <env_name>


## 3) Checking with equality for singletons
### Bad:

def equality_for_singletons(x):
    if x == None:
        pass
    if x == True:
        pass
    if x != False:
        pass


### Good Practice:

def equality_for_singletons(x):
    if x is None:
        pass
    if x is True:
        pass
    if x is not False:
        pass


## 4) Manual string formatting
### Bad:

name = "Mitnick"
age = 25


def manual_str_formatting(name, age):
    if age > 18:
        print("So cool" + name + ", you can legally drink alcohol!")
    else:
        print("Sorry, " + name + ", no booze for you.")


## instead use f strings:
def manual_str_format(name, age):
    if age > 18:
        print(f"So cool {name}, you can legally drink alcohol!")


## 5) Manual call close() / not using a context manager
### Gonna close ok if no error. If the write call throws an exception, the file will never be closed. Instead use a with statement, which will ensure the file is closed even if an exception is thrown:

def manually_calling_close_on_file(file):
    file = open("file.txt", "w")
    file.write("Hello")
    file.close()


### with statement: ensure no matter what happens that the file is gonna close

def manually_calling_close_on_file2(file):
    with open("file.txt", "w") as file:
        file.write("Hello")
