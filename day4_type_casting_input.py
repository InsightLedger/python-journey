# In python , the function input()is designed to read data from the user as text. 

 # input() always returns a value of type string (str) regardless of what the user type.

# python does not assume whether the input is
    •a number
    •a word
    •a symbol 
so,it treats everything as a string by default to avoid wrong assumption.

Type Conversion (overall concept)
│
├── Implicit Conversion (automatic)
└── Explicit Conversion (manual = Type Casting)

# type conversion = changing one data type to another.

#
  1. implicit conversion = python automatically convert data types to larger one to prevent data loss. 
ex-  
x=5       # int
y=2.5     # float
z=x+y    #pythoms converts int - float
print (z) #7.5