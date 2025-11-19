# Typecasting = the process of converting a variable from one data type to another data type
#               str() , int() , float() , bool()


name = "Alice"
age = 30  # age is a string
height = 5.7  # height is a float
is_student = True  # is_student is a string

print(f"Name: {name} (type: {type(name)})")
print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} (type: {type(height)})")
print(f"Is Student: {is_student} (type: {type(is_student)})")

# Typecasting
height = int(height)  # converting age to integer
age = float(age)  # converting height to float
age = str(age)  # converting age to string
print(f"After typecasting: {age} (type: {type(age)})")
print(f"After typecasting: {height} (type: {type(height)})")
print(f"After typecasting: {age} (type: {type(age)})")
