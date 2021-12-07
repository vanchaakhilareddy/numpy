#!/usr/bin/env python
# coding: utf-8

# # Create a null vector of size 10 but the fifth value which is 1

# In[9]:


import numpy as np
x=np.zeros(10)
x[4]=1
x


# # Create a vector with values ranging from 10 to 49.

# In[11]:


import numpy as np
x=np.arange(0,50)
print("vector:",x)


# # Create a 3x3 matrix with values ranging from 0 to 8

# In[15]:


import numpy as np
x=np.arange(0,9).reshape(3,3)
print("matrix:",x)


# # Find indices of non-zero elements from [1,2,0,0,4,0]

# In[16]:


import numpy as np
x=np.array([1,2,0,0,4,0])
x[x>0]


# # Create a 10x10 array with random values and find the minimum and maximum values

# In[17]:


import numpy as np
x=np.random.randint(1,100,(10,10))
print(x)
xmin=x.min()
xmax=x.max()
print("min value is:",xmin)
print("max value is:",xmax)


# In[ ]:




