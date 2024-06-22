#!/usr/bin/env python
# coding: utf-8

# ## Types of objects in Python
# 
# Python is a object-oriented language. There are many different types of objects in Python. Let's start with the most common object types: strings, integers and floats. Anytime you write words (text) in Python, you're using character strings (strings for short). The most common numbers, on the other hand, are integers (e.g. -1, 0, 100) and floats, which represent real numbers (e.g. 3.14, -42.0).
# 
# The following code cells contain some examples.

# In[1]:


#Integer 
11


# In[2]:


# Float

2.14


# In[3]:


# String
"Hello World"


# You can get Python to tell you the type of an expression by using the built-in type() function. You'll notice that Python refers to integers as int, floats as float, and character strings as str.

# In[4]:


# Type of 12
type(12)


# In[5]:


# Type of 2.14
type (2.14)


# In[7]:


# Type of Hello World
type("Hello world")


# ### Integers
# Integers can be negative or positive

# In[9]:


type(-1)


# type(1)

# ### Floats
# 
# Floats represent real numbers; they are a superset of integer numbers but also include "numbers with decimals". 

# In[11]:


type(1.0)


# In[13]:


type(0.5)


# In[14]:


type(-0.3)


# ### Converting from one object type to a different object type
# 
# You can change the type of the object in Python; this is called typecasting. 

# #### Converting integers to floats 

# In[15]:


float(2)


# In[16]:


type(float(2))


# #### Converting floats to integers
# 
# If we cast a float into an integer, we could potentially lose some information

# In[17]:


int(1.1)


# #### Converting from stings to integers or floats
# 
# Sometimes, we can have a string that contains a number wothin it. If this is tha case, we can cast that string that represents a number into an integr using int()

# In[18]:


# Convert a string into an integer
int("1")


# But if you try to do so with a string that is not a perfect match for a number, you'll get an error. Try the following:

# In[20]:


#Convert a string into an integer with error

int("1 or 2 people")


# You can also convert string containing floating point number into float objects:

# In[21]:


# Convert the string "1.2" into a float
float("1.2")


# #### Converting numbers to strings

# In[22]:


# Convert an integer to a string
str(1)


# In[23]:


# Convert a float to a string
str(1.2)


# ### Boolean data type
# Boolean is another important type in Python. An obect of type Booelean can take on one of two values: True or False:

# In[24]:


# Value true

True


# In[25]:


#Value False
False


# In[27]:


type(True)


# In[28]:


type(False)


# <p>We can cast boolean objects to other data types. If we cast a boolean with a value of <code>True</code> to an integer or float we will get a one. If we cast a boolean with a value of <code>False</code> to an integer or float we will get a zero. Similarly, if we cast a 1 to a Boolean, you get a <code>True</code>. And if we cast a 0 to a Boolean we will get a <code>False</code>. Let's give it a try:</p> 

# In[29]:


#Convert True to int
int(True)


# In[30]:


# Convert 1 to boolean
bool(1)


# ### Exercise: Types 

# What is he data type of the result of 6/2

# In[32]:


type(6/2)


# What is the data type of the result 6//2

# In[33]:


type(6//2)


# What is the data type of "Hello world"

# In[34]:


type("Hello world")


# What is the data type of "hello"=="world"

# In[35]:


type("hello"=="world")


# Write the code to convert the following number representing employeeid **"1001"** to an integer

# In[37]:


int(1001)


# Write the code to convert this number representing financial value **"1234.56"** to a floating point number

# In[39]:


float(1234.56)


# Write the code to convert this phone number **123-456-7890** to a string

# In[41]:


str("123-456-7890")

