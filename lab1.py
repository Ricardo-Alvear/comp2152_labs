from token import NUMBER

print("Hello")
print(3)

a = 5
print(a)

b = "Ricardo"
print(b)

print(a, b)

print(type(a), type(b))
print(type(9.0))
print(type(True))

# This is a comment

print(5 + 5)
print(5 - 5)
print(a * 5)

c = 3
d = 4
e = 5
f = 6
g = c + d ** e / f % e
h = c - d // e ** (f + d) * c

# 0. Parentheses ()
# 1. Powers **
# 2. Multiplication and division * /   // => to round up
# 3. Addition and subtraction + -
print(h)

l = [1,2,3,4]
print(l[3])

m = [1,2,3, "Five", 6.0]
print(m)

# string formatting
age = 5
print("My age is", age)
print("I am", age, "years old")

st_f = "I am {} {} years old"
st_not_f = "not"
print(st_f.format(st_not_f, age))

# user input
t =  input("Enter a number: ")
correctType = int(t)
total = 5 + correctType
num_Str = "Number is {}"
print(num_Str.format(total))
