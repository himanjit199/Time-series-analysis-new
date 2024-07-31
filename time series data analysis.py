#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install pandas-datareader')


# In[5]:


import pandas_datareader as pdr
import pandas as pd
from datetime import datetime


# In[7]:


import pandas as pd
from datetime import datetime


# In[9]:


pip install yfinance


# In[10]:


import yfinance as yf
import pandas as pd
from datetime import datetime

# Fetch the data for TSLA
tsla_data = yf.download('TSLA')

# Display the first few rows of the data
print(tsla_data.head())


# In[11]:


tsla_data.tail()


# In[13]:


tsla_data['High'].plot(figsize=(12,4))


# In[15]:


# xlimit,color 
tsla_data['High'].plot(xlim=['2022-01-01','2023-10-29'],figsize=(12,4),c='red',ls='--')


# In[16]:


index=tsla_data.loc['2022-01-01':'2023-10-29'].index
share_open=tsla_data.loc['2022-01-01':'2023-10-29']['Open']


# In[17]:


share_open


# In[18]:


import matplotlib.pyplot as plt


# In[19]:


figure,axis=plt.subplots()
plt.tight_layout()
## Preventing overlapping
figure.autofmt_xdate()
axis.plot(index,share_open)


# # Time resampling

# In[21]:


tsla_data.head()


# In[22]:


# Resample the Data: It resamples the tsla_data DataFrame using the rule 'A', which stands for "Annual". This means it will group the data by each calendar year
tsla_data.resample(rule='A').min()


# In[24]:


tsla_data.resample(rule='A').min()['Open'].plot()


# In[26]:


# Resample the Data: It resamples the tsla_data DataFrame using the rule 'QS', which stands for "Quartely"
tsla_data.resample(rule='QS').min()


# In[28]:


tsla_data['Open'].resample(rule='BA').mean().plot(kind='bar')


# In[31]:


# Monthly wise 
tsla_data['Open'].resample(rule='M').mean().plot(kind='bar',figsize=(30,4))


# In[32]:


tsla_data['High'].rolling(11).max().head(20)


# In[33]:


tsla_data['Open:30 days rolling']=tsla_data['Open'].rolling(30).mean()


# In[34]:


tsla_data.head(32)


# In[35]:


tsla_data[['Open','Open:30 days rolling']].plot(figsize=(12,5))


# In[ ]:




