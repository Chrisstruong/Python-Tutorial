# typecasting = the process of converting a value of one data type to another
#               (string, integer, float, boolean)
#               Explicit vs Implicit

name = ""
age = 0
gpa = 1.9
student = True

# All these examples are Explicit operations. Explicit mean converting data types manually
name = bool(name)
print(name)



# Below is the example of Implicit. Implicit typecasting can be converted when you perform certain operations on it
x = 2
y = 2.0

x = x / y

print(x)