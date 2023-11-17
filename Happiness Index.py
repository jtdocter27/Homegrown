#!/usr/bin/env python
# coding: utf-8

# ## How much of my money is making me happy? 

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


hi = pd.read_excel('Happiness Index(3).xlsx', 
                  header = 0) 
hi.head(20)


# In[4]:


hi.sum(axis = 0, numeric_only = True)


# In[5]:


hi = hi.sort_values(by='Ranking')


# In[6]:


hi.plot.bar(x = "Maslow's Category", y='Amount', figsize=(15,10), color = 'Grey')
plt.xticks(rotation = 45)


# In[10]:


sns.histplot(data=hi, x = 'Amount', y='Purchase Type', hue="Maslow's Category")


# In[13]:


sns.displot(data=hi, x="Amount", y="Purchase Type", col="Maslow's Category", 
    col_wrap=5, height= 4, aspect=0.9, col_order = ['Physiological','Safety','Love/Belonging','Esteem','Self-Actualization'])
sns.set_theme(palette = 'Spectral')


# ### To do list
# 1) Order by ranking 
# 2) Stylize 

# In[ ]:




