"""
========================================================
        PYTHON - LISTS & TUPLES - NOTES
========================================================
Topics covered:
1. Lists - basics (mutable), accessing, changing values
2. List slicing (and mutating a slice)
3. List methods - append, sort, sort(reverse), reverse,
   insert, remove, pop
4. Tuples - basics, indexing, index()
5. Tuple with single element - the comma rule
6. Tuple slicing (same as string slicing)
7. Tuple - index() and count()
8. Practice - store 3 favorite movies in a list
9. Practice - check if a list is a palindrome
10. Practice - count grade "A" in a tuple, sort a list
========================================================
NOTE: Uncomment ONE section at a time to run it.
========================================================
"""

# ---------------------------------------------------
# 1. LISTS - basics (mutable), accessing, changing values
# ---------------------------------------------------
# LIST IN PYTHON:   [ ,  ,  ,  ,] mutable

# list ku bhi ham variable ke jaisa naam dete .  andar koma se separate karte aur apna apna type ke mutabiq likhte .

# marks=["karan", "abbubakar", 56, 5.8 ]
# print(marks)
# print(marks[0]) # execcesing.
# marks[0]="khizer"
# print(marks[0]) # changing. since lists are  mutable .


# ---------------------------------------------------
# 2. LIST SLICING (and mutating a slice)
# ---------------------------------------------------
# LIST SLICING :

# marks=[23,43,56,23]
# print(marks[0:4])
# marks[0:4]=12,45,65,87 # mutating the values but it should match with there own class.
# print(marks[0:4]) #ek number bardhke lena kyu ki last waala count nai hota .


# ---------------------------------------------------
# 3. LIST METHODS - append, sort, reverse, insert, remove, pop
# ---------------------------------------------------
# METHODS OF LISTS :

# list = [ 6, 7, 9 , 2 ]
# list.append(4) 
# print(list)
# marks = [34 , 34, 56,  67 , 23, ]
# print(marks[0:4])
# print(marks[:])

# list.sort() # allign the elements in accending order.
# print(list)

# list.sort(reverse=True) #allign the elements in deccending order. 
# print(list)

# list.reverse()
# print(list)

# list.insert(3,34) # index 3 pe agaya element 34 .
# print(list)

# list.remove(9) remove the element directly by entering elements name.
# print(list)

# list.pop(1) # indx 1 pe 7 tha gayap hogaya. 
# print(list)
 

# ---------------------------------------------------
# 4. TUPLES - basics, indexing, index()
# ---------------------------------------------------
# TUPLES:
 
# tup=(34,"arjun",  24, 90, 56 )
# # print(type(tup))
# print(tup.index(90))
# print(tup[0])
# print(tup[1])


# ---------------------------------------------------
# 5. TUPLE WITH SINGLE ELEMENT - the comma rule
# ---------------------------------------------------
# NOTE: (6,) is a tuple, but (6) without a comma is just
# an int -- comma is what makes it a tuple.
#
# tup3=(6,)
# print(type(tup3))

# tup3=(6) 
# print(type(tup3)) # type int hojari isliye ham , bhi likhna agr sirf ek element likhre andar toh.


# ---------------------------------------------------
# 6. TUPLE SLICING (same as string slicing)
# ---------------------------------------------------
# SLICING IN TUPLE IS SAME AS SLISING IN STRINGS: 

# tup4= (4, 5, 6 ,7, 8)
# print(tup4[0:])
# print(tup4[0:3])


# ---------------------------------------------------
# 7. TUPLE - index() and count()
# ---------------------------------------------------
# hero=(3,5,7,3,6,2,)
# hero.index(5)
# print(hero)
# print(hero.index(5)) # returns index of 5 

# print(hero.count(3)) # returns no of times 3 comes .


# ---------------------------------------------------
# 8. PRACTICE - store 3 favorite movies in a list
# ---------------------------------------------------
# PRACTICE:

# WAP TO ASK A USER TO ENTER NAMES OF 3 FAVORITE MOVIES AND STORE THEM IN LIST :
# movies=[]
# m1=input("movie 1:")
# m2=input("movie 2:")
# m3=input("movie 3:")
# movies.append(m1)
# movies.append(m2)
# movies.append(m3)
# print(movies)


# ---------------------------------------------------
# 9. PRACTICE - check if a list is a palindrome
# ---------------------------------------------------
# LOGIC: copy the list, reverse the copy, compare with original.
# If same -> palindrome.
#
# WAP TO CHECK IF A LIST CONTAIN A PALINDROME OF ELEMENTS :

# list01= [ 1,2,1]
# list02= [ 1,2,3]
# list01_copy=list01.copy()
# list01_copy.reverse()
# list02_copy=list02.copy()
# list02_copy.reverse()

# if (list01_copy==list01):
#     print("palindrome")
# else:
#     print("not a palindrome")

# if (list02_copy==list02):
#     print("palindrome")
# else:
# #     print("not a palindrome")    
# list3=[3,4,4,3]
# list_3=list3.copy()
# list_3.reverse()
# if list_3==list3:
#     print("palindrome")
# else:
#     print("not palindome")


# ---------------------------------------------------
# 10. PRACTICE - count grade "A" in a tuple, sort a list
# ---------------------------------------------------
# WAP TO COUNT THE NO OF STUDENTS WITH THE GREADE "A" IN FOLLOWING TUPLE:

# tup01=("A","B","A","S","A","D","A")
# tup01.count("A")
# print(tup01.count("A"))

# list04 = ["C","D" ,"A","A","B","B","A" ] 
# list04.sort()
# print(list04)
