# let improt important packages, set working directory and 
# set up working directory 
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 


# In[2]:


# set of working dierction
os.chdir("C:\computational_skill\Machine learning\housing_price_prediction") # this is working directory of my PC.


# In[4]:


# let import data for analysis
housing = pd.read_csv('housePricePrdiction/housing.csv')
# then lets check data by info()
housing.info()


# In[5]:


# from above data we observe that data column = 10 , indexes = 20640 
# however there is missing indexes in total_bedrooms i.e it have total of 20433 
# there are different types of data float64 ( numerical data ) , total 9 column and 
# ocean_proximity data total 1 column. Let explore ocean_proximity column in more detail
housing['ocean_proximity'].value_counts()


# In[6]:


# different five categories of ocean_proximity column


# In[6]:


# lets explore data by describe()
housing.describe()


# In[8]:


# make histogram of data 
housing.hist(bins = 50, figsize=(20,15))
plt.show()   


# In[11]:


# data looks like housing_mdeian age is trun cut as 50 and 
# median_house_value is also trun cut at 50000

