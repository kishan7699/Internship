#!/usr/bin/env python
# coding: utf-8

# In[49]:


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.metrics import accuracy_score,confusion_matrix,roc_curve,roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns


# In[17]:


df = pd.read_csv('C:/Users/91954/data science pg program/mushrooms.csv')  
df


# In[50]:


df.describe()


# In[28]:


df.columns


# In[52]:


df.info()


# In[21]:


sns.scatterplot(x='cap-shape',y='class',data=df)


# we can see that the cap-shape is mostly equally distributed in the range of x and k
# 

# In[24]:


sns.scatterplot(x='cap-surface',y='class',data=df)


# we can see that the cap-surface is mostly equally distributed in the range of s and g

# In[25]:


sns.scatterplot(x='cap-color',y='class',data=df)


# we can see that the cap-color is mostly equally distributed in the range of n and r

# In[26]:


sns.scatterplot(x='bruises',y='class',data=df)


# we can see that bruiese has not much to conclude

# In[29]:


sns.scatterplot(x='odor',y='class',data=df)


# we can see that odor has been distributed in two diffrent portions of the plot which shows that they have diiferent conclusion for different odor

# In[51]:


sns.scatterplot(x='gill-attachment',y='class',data=df)


# In[ ]:


they 


# In[ ]:





# In[31]:


sns.scatterplot(x='gill-spacing',y='class',data=df)


# In[33]:


sns.scatterplot(x='gill-size',y='class',data=df)


# In[34]:


sns.scatterplot(x='gill-color',y='class',data=df)


# In[35]:


sns.scatterplot(x='stalk-shape',y='class',data=df)


# In[36]:


sns.scatterplot(x='stalk-root',y='class',data=df)


# In[37]:


sns.scatterplot(x='stalk-root',y='class',data=df)


# In[38]:


sns.scatterplot(x='stalk-surface-above-ring',y='class',data=df)


# In[39]:


sns.scatterplot(x='stalk-surface-below-ring',y='class',data=df)


# In[42]:


sns.scatterplot(x='veil-type',y='class',data=df)


# In[43]:


sns.scatterplot(x='veil-color',y='class',data=df)


# In[44]:


sns.scatterplot(x='ring-number',y='class',data=df)


# In[45]:


sns.scatterplot(x='ring-type',y='class',data=df)


# In[46]:


sns.scatterplot(x='spore-print-color',y='class',data=df)


# In[47]:


sns.scatterplot(x='population',y='class',data=df)


# In[48]:


sns.scatterplot(x='habitat',y='class',data=df)


# In[59]:


df.describe()


# In[60]:


df.shape


# In[ ]:




