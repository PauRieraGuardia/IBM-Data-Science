#!/usr/bin/env python
# coding: utf-8

# ## Expressions and Variables
# 
# ### Expressions
# 
# Expressions in Python con icnlude operations among compatible types. 

# In[2]:


# Addition operation expression

43 + 60 + 16 + 41


# We can perform subtraction operations using the minus operator. In the case the result is a negative number:

# In[3]:


# Subtraction operation expressiom

50 - 60


# We can do multiplication using an astersik: 

# In[4]:


5 * 5


# We can also perform division with the forward slash:

# In[5]:


# Division operation expression
25 / 5


# We can use the double slash for integer divisio, where the result is rounded down to the nearst integer:

# In[6]:


# Integer division operation expression
25 // 5


# In[7]:


25//6


# Let's write an expression that calculates how many hours there are in 160 minutes;

# In[10]:


160//60


# Python follows well accepted mathematical conventions when evaluating mathematical expressions. In the following example, Python adds 30 to the resul of multiplication.

# In[11]:


# Mathematical expresions
30 + 2*60


# In[12]:


(30 + 2) * 60


# ### Variables
# 
# Just like most programming languages, we can store values in variables, so we can use them later on. For example

# In[14]:


# Store value into variable

x = 43 + 60 +16 +41
x


# We can also perform operations on x and save the result to a new variable:

# In[15]:


y = x/2
y


# If we save a value to an existiting variable, the new value will overwrite the previos value:

# In[16]:


# Overwrite variable with new value

x = x/60
x


# ### Exercise: Expression in Python:
# 
# Write an expression to add 30 and 20 and subtract 40

# In[18]:


30 + 20 - 40


# Write an expression to subtract 5 form 55 and divide the result by 10 

# In[19]:


(55-5)/10


# Write an expression to multiply 6 woth 10 and divide the result by 12

# In[21]:


(6*10)/12


# ### Exercise: Variables in Python
# 
# What is the value of x where x =3+2*2

# In[24]:


x = 3 +2*2
x


# What is the value of y qhere y = (3+2)*2

# In[26]:


y = (3+2)*2
y


# What is the value of z where z =x+y

# In[27]:


z = x+y
z

