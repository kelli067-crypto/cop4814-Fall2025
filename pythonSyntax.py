"""
Basic Python Syntax
----------------------------
This file is a guided template for learning Python basics.
Students should fork and clone this repository from Greg's repo.
Explanations and examples will be added by Greg.
"""

# ==========================================================
# 1. PRINTING AND COMMENTS
# ----------------------------------------------------------
# - Print statements
# - Single-line comments
# - Multi-line comments (docstrings)
# ==========================================================

print("Greg", 3.14, 10)# this is a single line of coment

""""This is a block comment"""

# ==========================================================
# 2. VARIABLES AND DATA TYPES
# ----------------------------------------------------------
# - Strings
# - Integers, floats
# - Booleans
# - Type checking with type()
# ==========================================================

message = "Welcome to FIU"
print(type(message)) # type() is a function too

a = 10
b = 2
print(type(a),type(b))

isOpen = True
print(type(isOpen))

print(message[0])

# ==========================================================
# 3. BASIC OPERATORS
# ----------------------------------------------------------
# - Arithmetic (+, -, *, /, //, %, **)
# - Comparison (==, !=, >, <, >=, <=)
# - Logical (and, or, not)
# ==========================================================

print(a+b) # additon
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division
print(7/2) # division again
print(7//2) #intiger divison
print(a**b) # exponentiation
print(7%2) # Modulus (remainder of the division)

# ==========================================================
# 4. STRING OPERATIONS
# ----------------------------------------------------------
# - Concatenation
# - f-strings
# - Common methods (.upper(), .lower(), .strip(), etc.)
# ==========================================================

first_name = "Kenny"
last_name = "Ellis"

print(first_name + last_name)
print(first_name + " " + last_name) # 2 separate things
print(first_name, last_name)


print(f"My name is {first_name.upper()} {last_name.title()}.")# f is ised to format, the variable
print(2 +"3")# will make an error because they see the + as different things
print("2"+"3")# will put them together and make 23
print("***Welcome to Software Dev***".strip('*'))# removes the thing that is in the ()

# ==========================================================
# 5. LISTS
# ----------------------------------------------------------
# - Creating lists
# - Indexing and slicing
# - Adding/removing elements
# - Useful methods (.append(), .remove(), .sort(), etc.)
# ==========================================================

professors = ["greg","richard","kianoosh","debra","jason","leo","heather"]
print(type(professors))
print(professors[0])
print(professors[-1])# will give the last professor
print(professors[2:5])# will include the proffesors from 2-5, accessing 2,3 and 4
print(professors[:5])# will start form the begining 0-4
print(professors[3:])# all the way to the end 3-the end
print(professors[:])# print everything, and makes a copy of the list

professors.append("todd")# adds todd to the end of the list
print(professors)
professors.extend(["michael", "mustafa","naomi"])# multiple addings
print(professors)
professors.insert(2,"vyoma")#can insert someone
print(professors)
professors.remove("greg")
professors.pop(2)# will remove anyone in the position, can also save the position
print(professors)
x=professors.pop().pop(2)
print(professors,x)
professors.reverse()#reverse the original list
print(professors)
professors.sort()# will alpabetize ti
professors.sort(reverse=True)
print(professors)
# ==========================================================
# 6. TUPLES AND SETS
# ----------------------------------------------------------
# - Tuples: immutable sequences
# - Sets: unique collections
# ==========================================================

grades = (88.3, 78.6, 99.5)# tuples cant be modified
print(type(grades))
grades[0]=91.3

members = {"greg", "richard", "greg"}
print(members)# this is an answer of a fiu assignment

# ==========================================================
# 7. DICTIONARIES
# ----------------------------------------------------------
# - Key-value pairs
# - Accessing and modifying values
# - Common methods (.keys(), .values(), .items())
# ==========================================================



# ==========================================================
# 8. CONDITIONALS
# ----------------------------------------------------------
# - if, elif, else
# - Nested conditionals
# ==========================================================



# ==========================================================
# 9. LOOPS
# ----------------------------------------------------------
# - for loops
# - while loops
# - break and continue
# ==========================================================



# ==========================================================
# 10. FUNCTIONS
# ----------------------------------------------------------
# - Defining functions
# - Parameters and return values
# - Default arguments
# ==========================================================



# ==========================================================
# 11. IMPORTING MODULES
# ----------------------------------------------------------
# - Importing built-in modules (e.g., math, random)
# - Using functions from modules
# ==========================================================



# ==========================================================
# 12. ERROR HANDLING (OPTIONAL)
# ----------------------------------------------------------
# - try, except
# - Handling different exception types
# ==========================================================



