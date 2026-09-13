"""
========================================================
        PYTHON BASICS - NOTES
========================================================
Topics covered:
1. Variables, print(), type()
2. Boolean type
3. Arithmetic (subtraction, exponent **)
4. Relational (comparison) operators
5. Assignment operators (+=, **=)
6. Logical operators (and, or, not)
7. Type conversion (str())
8. Input in Python - basic input()
9. Input - type casting with int()
10. Input examples - storing input in variables first
11. Practice programs - sum, area, average, comparison
========================================================
NOTE: Uncomment ONE section at a time to run it.
========================================================
"""

# ---------------------------------------------------
# 1. VARIABLES, print(), type()
# ---------------------------------------------------
# name ="abuzar"
# age=14
#income=120
# income2= name 
# print(age+income) 
#print("hello hey there .","how are you?")
# print("my name is abbubakar.","my height is 5.8")
# print("name is" , income2)
# print(type(age))
# print(type(income2))
# print(type(income)) 


# ---------------------------------------------------
# 2. BOOLEAN TYPE
# ---------------------------------------------------
# c=True
# print(type(c))


# ---------------------------------------------------
# 3. ARITHMETIC - subtraction, exponent (**)
# ---------------------------------------------------
# a=8466
# b=466
# sum=a-b
# print(sum)
# # why
# # hello 
# # duniya
# print("atiya")
# print("my name is atiya.","my height." , income)
#j=5 
# o=3
# print(j**o)


# ---------------------------------------------------
# 4. RELATIONAL (COMPARISON) OPERATORS
# ---------------------------------------------------
# relational operators (comparinsion operators)
# k=23
# l=32
# print(k==l)
# print(l!=k)
# print(j>=o)
# print(k<=l)


# ---------------------------------------------------
# 5. ASSIGNMENT OPERATORS
# ---------------------------------------------------
# aj+=income  ->  aj = aj + income
# As**=aj     ->  As = As ** aj
#
# assingnment  operators 
# aj=20
# buddy= aj + income 
# print(buddy)
# print("buddy:",buddy)
# aj+=income
# print(aj)
# As=2
# As**=aj 
# print("sum:",As)


# ---------------------------------------------------
# 6. LOGICAL OPERATORS: and, or, not
# ---------------------------------------------------
# LOGICAL OPERATOS 

# a=25
# b=20
# print(not(a>b)) 
# val1=True
# val2=False
# print("and operator:", val1 and val2) 
# print("or operater:",val1 or val2)
# A=50
# b=20
# print("or operator:",(A==b) or (A>b))


# ---------------------------------------------------
# 7. TYPE CONVERSION
# ---------------------------------------------------
# TYPE CONVERSION 
# a = 192.88
# a=str(a)
# print(type(a))


# ---------------------------------------------------
# 8. INPUT IN PYTHON - basic input() (always returns str by default)
# ---------------------------------------------------
# INPUT IN PYTHON 
# name=input("sentence:")
# print("hello abuzar",name)
#hobby=input("my hobby:")
#print("hey mehdi do you know","my hobby is",hobby)
# val=input("enter some value:")
# print(type(val))


# ---------------------------------------------------
# 9. INPUT WITH TYPE CASTING - int(input(...))
# ---------------------------------------------------
# NOTE (in own words): without type casting, input() output
# always comes as str class. After type casting with int(),
# output class becomes int -- but only works when the value
# entered is actually castable (e.g. numbers only for int()).
#
#bol=int(input("mera naam:"))# my number jab mai khali numbar lerao tha without type casting toh mere out put ki class hamesha str ari thi magar ab type casting ke bad int me ari magr sirf jo hosakte unkohi lesakte example nubers only get type casted into int.
#print(type(bol))
# num=input("enter a number :")
# print(type(num))


# ---------------------------------------------------
# 10. INPUT EXAMPLES - store input in variable, then print later
# ---------------------------------------------------
# examples 
# name=input( "enter name:")
# age= input("enter age:")
# marks=input("enter marks:")

# print("welome buddy:" ,name )
# print("how old are you:", age)    VARIABLE ME LELO INPUT BADME VARIABLE pRINT KARALO!
# print("how much have you scored:",marks )
 
# school=(input("my school name:"))
# inter=(input("my junior college:"))
# engeeneering=(input("my engeeneering college:"))
# print("my school name:",school)
# print("my intermediate college name:", inter)
# print("my eng clg name:",engeeneering)


# ---------------------------------------------------
# 11. PRACTICE - sum, square area, rectangle area, average, comparison
# ---------------------------------------------------
# PRACTICE! 
# first=int(input("enter first:"))
# second=int(input("enter second:"))
# print("sum =",first + second)

# side1 = int(input("side1:"))
# side2 = int(input("side2:"))
# area = side1*side2
# print("my square area:",area)

# side=float(input("my square side:"))
# print("area=",side*side)

# ok=float(input("my point number 1:"))
# ji=float(input("my point number 2:"))
# print("avg=",(ok+ji)/2)

# a=int(input("a1:"))
# b=int(input("b1:"))
# print(a>=b)   
