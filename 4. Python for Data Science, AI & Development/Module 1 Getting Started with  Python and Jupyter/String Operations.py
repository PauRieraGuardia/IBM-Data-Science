#!/usr/bin/env python
# coding: utf-8

# ### What are Strings?
# 
# The following example shows a string contained within 2 quotation marks:

# In[1]:


# Use quatation marks for defining string

"Michael Jackson"


# We can also use a single quatation marks:

# In[2]:


# We can also use single quatation marks:

'Michael Jackson'


# A string can be combination of spaces and digits

# In[3]:


# Digitals and spcaes in string

"1 2 3 4 5 6 "


# A string can also be a combination of special characters:

# In[4]:


# Special characters in string
"@#~¬¬¬€"


# We can print our string using the print statement:

# In[5]:


# Print the string
print("hello")


# We can bind or assing a string to another variable:

# In[7]:


name = "Michael Jackson"
name


# ### Indexing 
# 
# It is helpful to think of a string as an ordered sequence. Each element in the sequence can be accessed using an index represented by the array of numbers:

# In[8]:


# Print the first element in the srting 
print(name[0])


# In[9]:


# Print the element on index 6 in the string
print(name[6])


# In[10]:


# Print the element on the 13th index in the string 
print(name[13])


# ### Negative Index
# We can also use negative indexing with strings:

# In[11]:


# Print the last element in the string
print(name[-1])


# In[12]:


# Print the first element in the string
print(name[-15])


# In[14]:


# Find the length of strign
len("Michael Jackson")


# ### Slicing
# 
# We can obtein multiple characters from a string using slicing, we can obtain the 0 to 4th and 8th the 12th element:

# In[15]:


# Take the slice on variable name woth only index 0 to index 3
name[0:4]


# In[16]:


#Take the slice on variable name woth only index 8 to index 11
name[8:12]


# ### Stride 
# 
# We can also input a stride value as follow, woth the "2" idnicating that we are selecting every second variable:

# In[17]:


# Get every second element. The elements on index 1, 3, 5...
name[::2]


# In[18]:


# Ger every second element in the range from indez 0 to index 4
name[0:5:2]


# ### Concatenate Strings
# 
# We can concatenate or combine strings using the addition symbols, and the result is a new string that is a combination of both:

# In[19]:


# Concatenate two strings

statement = name + "is the best"
statement


# In[22]:


# Print the string for 3 times
"Michael Jackson "*3


# In[24]:


# Concatenate strings
name = "Michael Jackson"
name = name +"is the best"
name


# ### Escape Sequences
# 
# Back slashes represent the beginning of escape sequences. Escape sequences represent strings that may be difficult to input. For example, back slash "n" represents a new line. The output is given by a new line after the back slash "n" is encountered: 

# In[25]:


# New line escape sequence 
print("Michael Jacskon \n is the best")


# In[26]:


# Tab escape sequence 
print (" Michael Jackson \t is the best")


# In[29]:


#  Include Back slash in string
print ("Michael Jacsokn \\ is the best")


# In[30]:


# r will tell python that string willbe display as raw string
print (r"Michael Jacskon \ is the best")


# ### String Manipulation Operations
# There are many string operation methods in Python that can be used to manipulate the data. We are going to use some basic string operations on the data.
# Let's try with method upper; thos method convert lower case characters to upper case characters:

# In[31]:


# Convert all the characters in string to upper case

a = "Thriller is the sixth studio album"
print("before upper:",a)
b = a.upper()
print("After upper:", b)


# The method replace a segment of the sting. We input the part of the string we would like to change. The second argument is what we would like to exchange the segment with, and the result is a new string with the segment changed:

# In[32]:


# Replace the old substring woth the new terget substring is the segment has been found in the string
a = "Michale Jacskon is the best"
b = a.replace("Michale","Janet")
b


# The method find finds a sub-string. the argument is the substring you would like to find, and the output is the first index of the sequence. We can find the sub-string jack or el .

# In[38]:


# Find the substring in the string. Only the index of the first element of substring in string will be the output
name ="Michael Jackson"
name.find("el")


# In[39]:


# Find the substring in the string
name.find("Jack")


# if the sub-string is not in the string then the output is a negative one.

# In[40]:


name.find("Jacskskff")


# The method split splits the string at the specified separator, and returns a list:

# In[41]:


#Split the substring into list
name = "Michael Jackson"
split_string=(name.split())
split_string


# ### RegEx
# 
# In Python, RegEx (shor for Regular Expression) is a tool for maching and handling strings.
# 
# This RegEx module provides several functions for working with regular expressions search, split, findall, and sub.
# 
# Python provides a built-in module called re which allows you to work with regular expressions. First, import the re module

# In[42]:


import re


# The search() function searches for specified patterns within a string. Here is an example that explains how to use the search() function to search for the word "Jackson" in the string "Michael Jacksom is the best".

# In[44]:


s1= "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string 
result = re.search(pattern, s1)

# Check if a match was found 
if result:
    print("Match found!")
else:
    print("Match not found")


# The findall() function finds all occurrences of a specified pattern within a string.

# In[45]:


s2= "Michael Jackson was a singer and known as the 'King of Pop'"

# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as",s2)

# Print put the list of matched words
print(result)


# The sub function of a regular expression in Python is used to replace all occurrences of a pattern in a string with a specified replacement.

# In[48]:


# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string)


# ### Quiz on Strings 
# 
# What is the value of the variable a after following code is executed?

# In[49]:


# Write your code below

a ="1"
a


# Consider the variable d use slicing to print out the first three elements:

# In[51]:


d = "ABCDEFG"
d[0:3]


# Use a stride value of 2 to print put every second character to the string e:

# In[52]:


e ="clocrkr1e1c1t"
e[::2]


# Print out a backslash:

# In[54]:


print(r"\ ")


# Convert the variable f to uppercase:

# In[55]:


f ="You are wrong"
f.upper()


# Convert the variable f2 to lowercase:

# In[57]:


f2 = "YOU ARE RIGHT"
f2.lower()


# Consider the variable g, and find the index of the sub-strinf snow:

# In[61]:


g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
g.find("snow")


# In the variable g, replace the sub-string Mary with Bob:

# In[63]:


g.replace("Mary", "Bob")


# In the variable g, replace the sub-string c with .:

# In[64]:


g.replace(",",".")


# In the variable g, split the substring to list:

# In[65]:


g.split()


# In the string s3, find wether the digit is present or not using the \d and search() function:

# In[66]:


s3 ="House number- 1105"
result=re.search("\d",s3)

if result:
    print("Digit Found")
else:
    print("Digit nof found")

