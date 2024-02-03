#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[2]:


file_path = r"C:\Users\vashi\Desktop\Sales Data.csv"
df = pd.read_csv(file_path, encoding='unicode_escape')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[8]:


df.info()


# In[9]:


df.isnull().sum()
df.dropna(inplace=True)


# In[10]:


df.isnull().sum()


# In[11]:


df['Amount'] = df['Amount'].astype('int')


# In[12]:


df['Amount'].dtypes


# In[13]:


df.columns


# In[14]:


df.rename(columns= {'Marital_Status':'Shaadi'})


# In[15]:


df.describe()


# In[16]:


df[['Age', 'Orders', 'Amount']].describe()


# In[17]:


plt= sns.countplot(x = 'Gender',data = df)

for bars in plt.containers:
    plt.bar_label(bars)


# In[18]:


sales = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales)


# In[19]:


plt= sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in plt.containers:
    plt.bar_label(bars)


# In[20]:


sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# In[21]:


sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[22]:


sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# In[23]:


plt= sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in plt.containers:
    plt.bar_label(bars)


# In[24]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# In[25]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# In[27]:


sns.set(rc={'figure.figsize':(15,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[28]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# In[29]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[30]:


import matplotlib.pyplot as plt

plt.clf()  # Reset the Matplotlib plot

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')

# Add labels and title as needed
ax1.set_xlabel('Product ID')
ax1.set_ylabel('Total Orders')
ax1.set_title('Top 10 Products by Total Orders')

# Show the plot
plt.show()


# In[ ]:




