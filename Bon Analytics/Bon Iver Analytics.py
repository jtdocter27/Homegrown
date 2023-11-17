#!/usr/bin/env python
# coding: utf-8

# ### Initial Imports

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
print('initial imports succesful')
# ### Reading in the Excel Sheet

# In[2]:


bi = pd.read_excel('Bon Iver Data.xlsx', parse_dates = ['Release Date'], index_col = 'Album')
bi = bi.sort_values(by='Release Date')
bi


# ### Pandas Intro Functions for Looking at Large Tables

# In[8]:


#bi.head()
#bi.info()
#bi.describe()
#bi.value_counts()


# ### Plot Album vs. Plays w/ song

# In[97]:


fig, ax = plt.subplots(figsize=(8, 8))
biplot = sns.scatterplot(x ='Album', y ="Plays", data = bi, hue='Song', palette = 'coolwarm')
plt.legend(bbox_to_anchor = (1.4,1.1))
plt.xticks(rotation = 45)


# ### Plot Album vs. Plays W/ Season 

# In[98]:


fig, ax = plt.subplots(figsize=(8, 8))
biplot = sns.scatterplot(x ='Album', y ="Plays", data = bi, hue='Season', palette = 'coolwarm')
plt.legend(bbox_to_anchor = (1.4,1.1))
plt.xticks(rotation = 45)


# ### Time vs. Plays

# In[99]:


sns.lmplot(x ="Time", y ="Plays", data = bi, order = 2, ci = None)


# # Summary Stats

# In[101]:


bialbum = bi.groupby('Album').sum()
bialbum


# In[102]:


biseason = bi.groupby('Season').sum()
biseason


# In[107]:


biplot2 = sns.scatterplot(x ='Season', y ="Plays", data = biseason, palette = 'deep')
plt.xticks(rotation=45)


# In[ ]:




