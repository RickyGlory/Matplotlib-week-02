#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


import matplotlib
import matplotlib.pylot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)


# In[ ]:


plt.plot([2, 5, 7, 11])
plt.ylabel('sumbu y')
plt.show()


# In[ ]:


plt.plot([2, 3, 4, 7], [5, 4, 2, 16])
plt.show()


# In[ ]:


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()


# In[ ]:


t = np.arange(0., 5., 0.2)
t


# In[ ]:


plt.plot(t, t, 'r--')
plt.plot(t, t**2, 'bs')
plt.plot(t, t**3, 'g^')
plt.show()


# In[ ]:


data = {'a': np.arange(50)
        'C': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

data


# In[ ]:


plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


# In[ ]:


names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]


# In[ ]:


plt,plot(names, values)
plt.show()


# In[ ]:


plt,scatter(names, values)
plt.show()


# In[ ]:


plt,bar(names, values)
plt.show()

