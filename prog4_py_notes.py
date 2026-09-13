"""
========================================================
        PYTHON - DICTIONARIES - NOTES
========================================================
Topics covered:
1. Dictionaries - basics (key-value pairs)
2. Accessing values by key
3. Assignments on dict - updating an existing key's value
4. Adding a new key, overwriting a value's type
5. Nested dictionaries
6. Dict methods - keys(), values(), items()
7. len() on a dict / on its keys list
8. Accessing with [] vs .get() (and error vs None on missing key)
9. update() method - adding/merging key-value pairs
========================================================
NOTE: Uncomment ONE section at a time to run it.
========================================================
"""

# ---------------------------------------------------
# 1. DICTIONARIES - basics (key-value pairs)
# ---------------------------------------------------
# DICTIONARIES:

# dict={"name":"abbubakar",
#       "marks":95,
#       "topic":("dictionary","sets")}
# # print(dict)


# ---------------------------------------------------
# 2. ACCESSING VALUES BY KEY
# ---------------------------------------------------
# info={"greet":"goodmorning","grade":"A"}
# print(info["greet"])
# print(info["grade"])
 

# ---------------------------------------------------
# 3. ASSIGNMENTS ON DICT - updating an existing key's value
# ---------------------------------------------------
# # ASSIGNMENTS ON DICT:
# festivals={"eid":"ramzan","1stjan":"new year"}
# print(festivals["eid"])
# festivals["eid"]="bakraid"
# print(festivals["eid"])


# ---------------------------------------------------
# 4. ADDING A NEW KEY, overwriting a value's type
# ---------------------------------------------------
# NOTE: books["lang"]=2 overwrites the string value with an
# int -- shows dict values can be reassigned to any type.
#
# ADDING A NEW KEY
 
# books={"science":"bio,phy,chem","lang":"eng,telgu"}
# print(books["lang"])
# books["lang"]="arabic"
# print(books)
# books["theory"]="UHV"  # adding
# print(books)
# books["lang"]=2   # new value overwrite .
# print(books)
# nul_dic={}
# nul_dic["num"]=23
# print(nul_dic)


# ---------------------------------------------------
# 5. NESTED DICTIONARIES
# ---------------------------------------------------
# NESTED DICTIONARIES :

# students={ "name":"zain",
#           "subjects": {"phy":30,"math":30,"uhv":27}}
# print(students["subjects"]["phy"])
# print(students["subjects"]["uhv"])


sub={"math":30,"phy":30,"uhv":27}

# ---------------------------------------------------
# 6. DICT METHODS - keys(), values(), items()
# ---------------------------------------------------
# print(sub.keys())
# print(list(sub.keys()))

# # to get total noof kyevalue pairs :
# print(len(sub))
# print(len(list(sub.keys())))
# print(sub.values())
# print(list(sub.values())) # list me store karae apn dict ku.

# print(sub.items()) # returns values in tuple.
# print(list(sub.items()))
# pairs=(list(sub.items()))
# print(pairs[0])
 

# ---------------------------------------------------
# 7 & 8. ACCESSING WITH [] vs .get() -- error vs None on missing key
# ---------------------------------------------------
# NOTE: dictname["missing_key"] raises an error, but
# dictname.get("missing_key") returns None instead.
# We mainly use dictname.get("specific key name") to be safe.
#
# print(sub["math"])
# print(sub.get("math"))

# print(sub["chem"]) # returns error 
# print(sub.get("chem")) # returns none 
# we mainly use dictname.get("specific key name")


# ---------------------------------------------------
# 9. update() METHOD - adding/merging key-value pairs
# ---------------------------------------------------
# NOTE: duplicate keys are not allowed, so if a key already
# exists (like "math" in pt), update() overwrites its value.
#
# sub.update({"social":30})
# # print(sub)
# pt={"cricket":"batball","math":"superb"}
# (sub.update(pt)) # since math already exists it will get overwrite ,(duplicate keys not allowed na isliye .)
# print(sub)
# sub["eng"]=34
# print(sub)
