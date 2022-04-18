from collections import namedtuple

# Without namedtuple
def divMod(x, y):
    return (x // y, x % y)

dm = divMod(100, 13)
# Confusing as to what are dm[0], dm[1]
print(type(dm)) # prints <class 'tuple'>
print(dm[0], dm[1])

# with namedtuple
def divMod(x, y):
    # First argument to namedTuple is name of this data type and then 
    # fields can be mentioned in 3 ways:
    # 1. List of strings - ["quotient", "remainder"]
    # 2. Whitespace Separated String - "quotient remainder"
    # 3. Comma Separated String - "quotient, remainder"
    DivModResult = namedtuple("DivMod", "quotient, remainder")
    return DivModResult(x // y, x % y)

dm = divMod(100, 13)
# Accessing using .operators with meaningful names. Similar to Kotlin inline classes.
print(type(dm)) # prints <class '__main__.DivMod'>
print(dm.quotient, dm.remainder)

# Other cool features
# 1. Defaults
Person = namedtuple("Person", "name job", defaults=["Python Developer"])
p = Person("Arjit")
print(p.name, p.job)

# Get as dictionary
print(p._asdict())
p = p._replace(job="Android Developer")
print(p)
