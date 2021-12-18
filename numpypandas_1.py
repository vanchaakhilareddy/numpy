#!/usr/bin/env python
# coding: utf-8

# ###### Importing the necessary libraries

# In[5]:


import pandas as pd
import numpy as np


# ###### Importing the dataset

# In[6]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'

users = pd.read_csv(url, sep= "|")


# In[8]:


#to know top 5 rows
users.head()


# ###### Assigning 'user_id' as index

# In[9]:


users = users.set_index('user_id')


# In[10]:


users.head()


# ###### First 10 and Last 10 entries

# In[11]:


print('--------First 10 entries -------')
users.head(10)


# In[12]:


print('--------Last 10 entries -------')
users.tail(10)


# ###### Number of observations in the dataset

# In[13]:


users.count()


# ###### Number of columns in the dataset

# In[14]:


print('Number of columns :', users.shape[1])
# print(users.shape[1])


# ###### Printing the name of all the columns.

# In[15]:


print('Name of all the columns:',(users.columns))


# ###### Dataset indexing

# In[ ]:


# users = users.Index()


# ###### checking the data type of each column

# In[17]:


users.dtypes


# ###### Printing only the occupation column

# In[18]:


print(users['occupation'])


# ###### counting different occupations in this dataset

# In[19]:


users['occupation'].nunique()


# In[20]:


users['occupation'].count()


# ###### What is the most frequent occupation

# In[21]:


df = pd.DataFrame(users)


# In[22]:


df['occupation'].value_counts(ascending=False).head(1)


# ###### DataFrame Info

# In[23]:


users.info()


# In[24]:


#Summarize only the occupation column has done already.
users['occupation'].value_counts()


# ###### Calculating mean age of users

# In[25]:


users['age'].mean()


# ###### What is the age with least occurrence

# In[26]:


users['age'].min()


# In[ ]:




