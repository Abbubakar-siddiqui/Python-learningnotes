"""
========================================================
        PYTHON - STRINGS & CONDITIONALS - NOTES
========================================================
Topics covered:
1. Strings - 3 types (single, double, triple quotes)
2. Escape sequence characters (\n, \t)
3. String concatenation
4. String length - len()
5. Indexing (and why strings are immutable)
6. Slicing (including negative index)
7. String functions - endswith(), capitalize(), replace(),
   find(), count()
8. Practice - first name length, occurrence of "$"
9. Conditional statements - if/elif/else basics
10. Conditional - traffic light example
11. Conditional - grading system (two versions)
12. Nested if
13. Practice - odd/even, greatest of 3, greatest of 4,
    multiple of 7
========================================================
NOTE: Uncomment ONE section at a time to run it.
========================================================
"""

# ---------------------------------------------------
# 1. STRINGS - 3 types
# ---------------------------------------------------
# STRINGS:

#they are of three types
# str1="its me k" 
# str2='how are you'
# str3=""" are you okay?"""  (multi line string.)


# ---------------------------------------------------
# 2. ESCAPE SEQUENCE CHARACTERS
# ---------------------------------------------------
# # ESCAPE SEQUENCE CHARACTERS:

#  1. \n for next line.
#str4="This is my car.\nit is my new car."
#print(str4)

#  2. \t for tab space .
# str5=("hey there buddy.\thow are you")
# print(str5)
#kite="why this all again. \nits my choice."
#print(kite)


# ---------------------------------------------------
# 3. STRING CONCATENATION
# ---------------------------------------------------
# BASICS OPERATIONS ON STINGS:
# 1: CONCATINATOIN: yani simply addition of two strings.
# stra = "abbu"
# strb = "bakar"
# finalstr=stra+strb
# print(stra+strb)
# a=int(input("a:"))
# b=int(input("b:"))
# print("sum:",a+b)      # NOTE :var define kare aur input se pehle int nai liye toh wo strich rehta add woye nai hota sirf chipak jata agr int bolke pehle liye tohich sahi kam karta. 


# ---------------------------------------------------
# 4. STRING LENGTH - len()
# ---------------------------------------------------
# 2: lenth of string : len(string name likhna)
# str7="abbubakar"
# str8="jeks"
# print(len(str7))
# print(len(str8))
# str9=str8+str7
# print(len(str9))
# str10= str7+"  "+str9
# print(len(str10)) # also count space as a length. 


# ---------------------------------------------------
# 5. INDEXING
# ---------------------------------------------------
# INDEXING:

# str11="siddiqui"
# # print(str11[3]) # since indexing start from zero.
# # print(str11[7])
# print(len(str11))
# print(str11[2])
# str[4]= p # we cannot assign any value by indexing only we can access characters.


# ---------------------------------------------------
# 6. SLICING (including negative index)
# ---------------------------------------------------
#SLICING: yani accesing part of a string .
# its comand will be stringname[starting index:ending index]
# str12="garibinsan"
# # print(str12[3:6])
# print(str12[ :10])
# print(str12[ :len(str12)])
# print(len(str12))
# print(str12[ : ])
# print(str12[ : len(str12)]) 
# negative index : 
# str13="apple"
# print(str13[-5:-1])
# print(str13[-5:]) 
#print(str13[-3:-1])


# ---------------------------------------------------
# 7. STRING FUNCTIONS - endswith, capitalize, replace, find, count
# ---------------------------------------------------
# STRINGFUNTIONS IN PYTHON: 
# strc=" i am a coder"
# strc.endswith("er")
# print(strc.endswith("er"))
# strd="its me your buddy"
# print(strd.endswith("dy"))
# print(strd.endswith("do"))

# stre="i am abbubakar"   # string ka naam hai str(e)
# print(stre.capitalize())
# print(stre)
# stre=stre.capitalize()
# print(stre)

# strf="hey there how are you buddy plz be happy"
# print(strf.replace("plz","please"))
# print(strf.replace("e","o"))
# strf=strf.replace("plz","please")
# print(strf.replace("e","o"))                  

#strf=" jao yaro jao pardhrao mai "
# print(strf.find("pardhrao"))  #shows 1st index of our required word.
# print(strf[14])   # shows index character                 
#print(strf.find("o"))  # space bhi index me count hota .

# strg="i am studying python."
# print(strg.count("o")) 
# print(strg.count("i")) 
# print(strg.count("t")) 

# q="nai arao mai njoy"
# p=q.find("njoy")
# print(p)
# print(q[13])


# ---------------------------------------------------
# 8. PRACTICE - first name length, occurrence of "$"
# ---------------------------------------------------
# WAP TO INPUT USERS FIRST NAME AND PRINT ITS LENGTH:
# name=input("my first name:")
# print(len(name))

# WAP TO FIND THE OCCURANCE OF "$" IN A STRING:
# string="in america we use $"
# print(string.find("$")) 
# print(string.count("a")) 
# ring=" hajrabegum"
# print(len(ring))
# print(ring.count("b")) 


# ---------------------------------------------------
# 9. CONDITIONAL STATEMENTS - if/elif/else basics
# ---------------------------------------------------
# NOTE (in own words): agar dono if/elif false dere (sahi nahi
# baithre) toh else kaam karta. else mein condition nahi likha
# ja sakta, sirf tab execute hota hai jab upar wale sab false hon.
#
# CONDITIONAL STATEMENTS: 
# age=18
# if(age>18):
#     print("can vote and apply for licence")
# elif(age<18):
#     print("cannot vote")  #AGR DONO FALSE DERE SAHI NAI BAITHRE TOH ELS KAM KARTA
# else   :  #isme condition nai likhaja sakta only execute when above all are false.
#     print("false")


# ---------------------------------------------------
# 10. CONDITIONAL - traffic light example
# ---------------------------------------------------
# light=input("light:")
# if(light=="red"):
#     print("stop")
# elif(light=="yellow"):
#     print("ready") 
# elif(light=="green"):
#     print("go")    
# else: 
#     print("go")      

# num=11
# if(num>=8):
#     print("njoy")
# if(num>10):
#     print("happiness")


# ---------------------------------------------------
# 11. GRADE OF THE STUDENTS (two versions)
# ---------------------------------------------------
# GRADE OF THE STUDENTS 
# marks=int(input("marks of my students:"))
# if(marks>=90):
#     grade="A"
# elif(90>marks>=80):    
#     grade="B"
# elif(80>marks>=70):
#     grade="C"
# elif(70>marks>=60):          
#     grade="D"
# print("grade of the student:",grade)  
 
  
# buddy 2
# marks=int(input("marks of my students:"))
# if(marks>=90):
#     grade="A"
# elif(marks<90 and marks>=80):    
#     grade="B"
# elif(marks<80 and marks>=70):    
#     grade="C"
# elif(marks<70 and marks>=60):    
#           grade="D"
# print("grade of the student:",grade)    


# ---------------------------------------------------
# 12. NESTING (if inside if)
# ---------------------------------------------------
# NESTING:

# age=90
# if(age>=18):
#     if(age>=80):
#         print("cannot drive")
#     else:
#         print("can drive")


# ---------------------------------------------------
# 13. PRACTICE - odd/even, greatest of 3, greatest of 4, multiple of 7
# ---------------------------------------------------
#practice
# WAP TO CHECK IF A NUMBER ENTERED BY THE USER ID ODD OR EVEN  :
# num=int(input("my number:"))
# remainder = num % 2 
# if(remainder==0):
#     print("Even")
# else:
#     print("odd")

# WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY USER:

# a=8900
# b=74570
# c=800
# if(a>b and a>c):
#     print("a")
# elif(b>a and b>c):
#     print("b")
# else: 
#     print('c')  


# d = int(input("first number = "))
# e = int(input("second number = "))
# f = int(input("third nubber = "))
# g = int(input("fourth number = "))
# if(d>=e and d>=f and d>g):
#     print("first number is largest",d)
# elif(e>=f and e>g):
#     print("second number is largest",e)
# elif(f>=g):
#     print("third number is largest",f)
# else:
#     print("fourth number is largest", g) 

# WAP tO CHECK IF A NUMBER IS MULTIPLE OF 7 OR NOT :

# digit=int(input("my number:"))
# rem= digit % 7 
# if(rem==0):
#     print("digit is multiple of 7:",digit)
# else:
#     print("not a multiple of 7")
