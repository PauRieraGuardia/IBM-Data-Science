#!/usr/bin/env python
# coding: utf-8

# ### Wha are Dictionaries?
# 
# A dictionary consists of keys and values. It is heplful to copare a dictionary to a list. Inseat of being ndexed numerically lika a list, dictionaries have keys. These eys are the keys that are used to access values within a dictionary.
# 
# The best example of a dictionary can be accessing person's detais using the social security number.
# Here the social security number which is a unique nuber will be the <b>key</b> and the details of the people will be the <b>values</b> associated

# ### Create a Dictionary and access the elements
# 
# An example of a Dictionary Dict: Here we are creatin a dictionary named <b>Dict</b> with he following details
# 
# * Keys are <b>key1</b>,<b>key2</b>,<b>key3</b>,<b>key4</b>,<b>key5</b>
# * Values are {1,2,[3,3,3],(4,4,4),5,(0,1):6} corresponding to the keys

# In[1]:


# Create the dictionary 

Dict ={"key1":1,"key2":"2","key3":[3,3,3], "key4":(4,4,4),("key5"):5,(0,1):6}
Dict


# The keys can be strings:

# In[2]:


# Access to the value ny the key
Dict["key1"]


# Keys can also be ay immutable object such as a tuple:

# In[3]:


# Access to the value ny the key
Dict[(0,1)]


# Each key is separated from its value by a colon ":". Commas separate the items, and the whole dictionary in enclosed in curly braces, like this "{}".

# In[4]:


# Create a sample dictionary 

release_year_dict = {"Thriller":"1982","Black in Black":"1980",
                    "The Dark Side of the Moon":"1973", "The Bodyguard":"1992",
                    "Bat Out of Hell":"1977","Their Greatest Hits (1971-1975)":"1976",
                    "Saturday Night Fever":"1977","Rumours":"1977"}
release_year_dict


# In summary, like a list, a dictionary holds a sequence of elements. Each element is represented by a key and its corresponding value. Dictionaries are created with two curly braces containing keys and values separated by a colon. For every key, there can only be one single value, however, multiplie keys can hold the same values. Keys can only be strings, numbers or tuples, but vaues can be any data tuype.

# ### Keys 
# 
# You can retrive the values based on the names:

# In[5]:


# Get value by keys

release_year_dict["Thriller"]


# In[6]:


# Get value by keys

release_year_dict["The Bodyguard"]


# Now lets us retrive the keys of the dicionary using the method keys():

# In[9]:


# Get all the keys in dictionary 

release_year_dict.keys()


# You can retrive the values using the method values()

# In[11]:


# Get all the values in dictionary

release_year_dict.values()


# We can add an entry:

# In[12]:


# Append value tih key into dicitonary

release_year_dict["Graduation"]="2007"
release_year_dict


# We can delete an entry:

# In[13]:


# Delete entries by key
del(release_year_dict["Thriller"])
del(release_year_dict["Graduation"])
release_year_dict


# We can verify if an element is in the dictionary:

# In[14]:


# Verify the key is in the dictionary

"The Bodyguard" in release_year_dict


# ### Quiz on Dictionaries 

# In[15]:


# Question sample dictionary

soundtrack_dic={"The Bodyguard":"1992","Saturday Night Fever":"1977"}
soundtrack_dic


# a) In the dictionary soundtrack_dic what are the keys?

# In[16]:


soundtrack_dic.keys()


# b) In the dictionary soundtrack_dic what are the values?

# In[17]:


soundtrack_dic.values()


# The Albums <b>Back in Black</b>, <b>The Bodyguard</b>, and <b>Thriller</b> have the following music recording sales in millons 50, 50 and 65 respectively:
# 
# a) Create a dictionary album_sales_dict where the keys are the album name and the sales in millions the values.

# In[21]:


album_sales_dict={"Back in Black":50, "The Bodyguard":50,"Thriller":65}
album_sales_dict


# b) Use the dictionary to find the total sales of <b>Thriler</b>

# In[22]:


album_sales_dict["Thriller"]


# c) Find the names of the albums from the dictionary using the method keys()

# In[23]:


album_sales_dict.keys()


# d) Find the values of the recording sales from the dictionary using method values:

# In[25]:


album_sales_dict.values()


# ### Scenario: Inventory Store
# 
# The inventory store scenario project utilizes a dictionary-based approach to develop a robust system for managing and tracking inventory in a retail store. 

# ### Task-1 Create an empty dictionary 
# 
# First you nedd to create an empty dictionary, where you will be stroing the product details:

# In[62]:


inventory={}


# ### Task-2 Store the firt producti details in variable
# 
# * Product name = Mobile Phone
# * Product Quantity = 5
# * Product price= 20000
# * Product Release Year = 2020

# In[63]:


product1_name="Mobile Phone"
product1_quantity=5
product1_price=20000
product1_release_year=2020


# ### Task-3 Add the details in inventory

# In[64]:


inventory["Product1_name"]= product1_name
inventory["Product1_quantity"]= product1_quantity
inventory["Product1_price"]= product1_price
inventory["Product1_release_year"]= product1_release_year
inventory


# ### Task-4 Store the second product details in a variable
# 
# * Product Name = "Laptop"
# * Product Quantity = 10
# * Product price = 50000
# * Product Release Year = 2023

# In[65]:


product2_name = "Laptop"
product2_quantity = 10
product2_price = 50000
product2_release_year = 2023


# ### Task-5 add the item detail in the inventory

# In[66]:


inventory["Product2_name"] =product2_name
inventory["Product2_quantity"] =product2_quantity
inventory["Product2_price"] =product2_price
inventory["Product2_release_year"] =product2_release_year
inventory


# ### Task-6 Display the Products present in the ivnentory 
# 
# Use print statement for fidplaying the products

# In[67]:


print(inventory)


# ### Task-7 Check if prodcut1_release_year and product2_release_year is in the invetory 

# In[68]:


"Product1_release_year" in inventory 


# In[69]:


"Product2_release_year" in inventory


# ### Task-8 Delete release year of both the prodcuts from the inventory 

# In[70]:


del(inventory["Product1_release_year"])
del(inventory["Product2_release_year"])
inventory

