#!/usr/bin/env python
# coding: utf-8

# ## Name: Kunal Jolly Saxena
# 

# # Data Analysis of a Super Store Dataset

# **This Exploratory Data Analysis focuses on a superstore, aiming to identify areas of improvement where the store can enhance its profitability. By thoroughly exploring the dataset, the analysis provides valuable insights into potential challenges that the business may encounter.**

# Let us import all the necessary libraries using their common aliasing and set some of the default styles for the plots.

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# ## Gathering and Extracting the Data from Data set

# Reading the csv file into a pandas dataframe.

# In[2]:


# Read the dataset into a pandas DataFrame
df = pd.read_csv('superstore_dataset.csv')

# Group the data by region and calculate the total sales and profit
region_data = df.groupby('Region').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

# Extract relevant columns for geographic analysis
geo_df = df[['Country', 'State', 'City', 'Sales', 'Profit']]

# Calculate total sales and profit by country
country_sales = geo_df.groupby('Country')['Sales'].sum().reset_index()
country_profit = geo_df.groupby('Country')['Profit'].sum().reset_index()


# In[3]:


df


# In[4]:


df['Region'].unique()


# In[5]:


df.columns


# In[6]:


df['Ship Mode'].unique()


# In[7]:


df['City'].nunique()


# In[8]:


df.info()


# As we can see, the data does not hold any null values. So, we need not process this data any more.

# In[9]:


df.describe()


# **As we can observe, there are no null values in any of the columns. So, our data is clean and no need to modify the existing columns but add some useful columns to it which help in visualizing the profits relatively. Lets calculate the profit percentage on each sale of the item and add that new column to our df.**

# In[10]:


df['Profit %']=df['Profit']/df['Sales']*100


# In[11]:


df['Profit %']


# ***Thus, we have now got our new column in the df. we can now proceed for out exploration of data of different columns.***

# ## Exploring and Visualizing the Data 

# **-> It is very much essential to analyze the data by grouping it based on category inorder to figure out the areas to be improved.**

# ### 1.Category wise distribution of profit and sales:

# Thus, we group the data by category and then by sub-category and aggregate them over sum to explore the data in depth. we then inspect the sales column and profit column.

# In[12]:


category_df= df.groupby('Category')[['Sales','Profit']].sum()


# Let us also calculate the percentage of the profit achieved over total sales in each category.

# In[13]:


category_df['profit %']=category_df['Profit']*100/category_df['Sales']


# In[14]:


category_df


# **A pie chart best suits for displaying the contributions of each category in the total profit. So why not plot one?**

# In[15]:


plt.figure(figsize=(12,6))
plt.title('Contribution of each category in Total Profit')
plt.pie(category_df.Profit, labels=category_df.index, autopct='%2.2f%%', startangle=180);


# ***These numbers clearly indicate that Furniture is not profitable to the expected extent though its overall sales are similar to that of remaining categories.***

# **Now that we have come to know that Furniture is the area to be taken into consideration, lets inspect the contribution of each sub-category of Furniture.**

# In[16]:


# Plot the total sales by region
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=region_data)
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()


# In[17]:


# Plot the total profit by region
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Profit', data=region_data)
plt.title('Total Profit by Region')
plt.xlabel('Region')
plt.ylabel('Profit')
plt.show()

# Group the data by country and calculate the total sales and profit
country_data = df.groupby('Country').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()


# In[18]:


# Calculate total sales and profit by state
state_sales = geo_df.groupby('State')['Sales'].sum().reset_index()
state_profit = geo_df.groupby('State')['Profit'].sum().reset_index()


# In[19]:


# Plot total sales by state
plt.figure(figsize=(12, 6))
sns.barplot(x='State', y='Sales', data=state_sales)
plt.title('Total Sales by State')
plt.xticks(rotation=45)
plt.show()


# In[20]:


# Plot total profit by state
plt.figure(figsize=(12, 6))
sns.barplot(x='State', y='Profit', data=state_profit)
plt.title('Total Profit by State')
plt.xticks(rotation=45)
plt.show()


# In[21]:


# Calculate total sales and profit by city
city_sales = geo_df.groupby('City')['Sales'].sum().reset_index()
city_profit = geo_df.groupby('City')['Profit'].sum().reset_index()


# In[22]:


# Plot total sales by city (top 10 cities by sales)
top_cities_sales = city_sales.nlargest(10, 'Sales')
plt.figure(figsize=(12, 6))
sns.barplot(x='City', y='Sales', data=top_cities_sales)
plt.title('Total Sales by City (Top 10)')
plt.xticks(rotation=45)
plt.show()


# In[23]:


# Plot total profit by city (top 10 cities by profit)
top_cities_profit = city_profit.nlargest(10, 'Profit')
plt.figure(figsize=(12, 6))
sns.barplot(x='City', y='Profit', data=top_cities_profit)
plt.title('Total Profit by City (Top 10)')
plt.xticks(rotation=45)
plt.show()


# ***This code, we use the `scatterplot()` function to create a scatter plot. The `x` parameter specifies the column to be plotted on the x-axis (`Sales`), and the `y` parameter specifies the column to be plotted on the y-axis (`Profit`). The `data` parameter takes the DataFrame (`df`) as input.***

# In[24]:


# Scatter Plot Example with Different Colors for Sales and Profit
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Sales', y='Profit', data=df, hue=df['Profit']>0)
plt.title('Sales vs Profit')
plt.show()


# In[60]:


# Sales Analysis
sales_by_location = df.groupby('City')['Sales'].sum().reset_index()

# Sort the cities by sales in descending order and select the top 10
top_10_cities = sales_by_location.nlargest(10, 'Sales')

# Line Plot: Top 10 Cities by Sales
plt.figure(figsize=(12, 6))
sns.lineplot(x='City', y='Sales', data=top_10_cities)
plt.title('Top 10 Cities by Sales')
plt.xticks(rotation=45)
plt.show()


# In[26]:


furniture_df=df[df['Category']=='Furniture']


# In[27]:


sub_category_df= furniture_df.groupby('Sub-Category')[['Sales','Profit']].sum()


# In[28]:


sub_category_df['profit %']=sub_category_df['Profit']*100/sub_category_df['Sales']


# In[29]:


sub_category_df


# ***Therefore, the sub-categories of Furniture-(Bookcases and Tables)are the ones to be taken care of to improve the profits.***

# **Perform the same analsyis for Office supplies and Technology categories to know which sub-categories of them are contributing to what extent.**

# In[30]:


office_supplies_df=df[df['Category']=='Office Supplies']


# In[31]:


sub_category_df1= office_supplies_df.groupby('Sub-Category')[['Sales','Profit']].sum()


# In[32]:


sub_category_df1['profit %']=sub_category_df1['Profit']/sub_category_df1['Sales']*100


# In[33]:


sub_category_df1


# We can observe that Paper and Binders are the major contributing factors for profit, thus there is a need to maintain the stability of these products with same profit , while the supplies are being sold for losses, which indicates that prices of the supplies have to be increased and bring them into profits.

# In[34]:


Technology_df=df[df['Category']=='Technology']


# In[35]:


sub_category_df2= Technology_df.groupby('Sub-Category')[['Sales','Profit']].sum()


# In[36]:


sub_category_df2['profit %']=sub_category_df2['Profit']*100/sub_category_df2['Sales']


# In[37]:


sub_category_df2


# **Now, its time to compare all the three categories along with their sub-categories in a single plot side by side. A bar chart can serve our purpose.**

# In[38]:


fig, axes = plt.subplots(1, 3, figsize=(20, 6))

axes[0].set_title('Profit percentage of each category in Furniture')
sns.barplot(x=sub_category_df.index,y=sub_category_df['profit %'],ax=axes[0])

axes[2].set_title('Profit percentage of each category in Technology')
sns.barplot(x=sub_category_df2.index,y=sub_category_df2['profit %'],ax=axes[2]);

axes[1].set_title('Profit percentage of each category in Office Supplies')
sns.barplot(x=sub_category_df1.index,y=sub_category_df1['profit %'],ax=axes[1]);

axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45, ha='right');


# ***These plots show that the maximum percentage of profits are coming from Offile supplies, while the loss is occuring majorly due to sub categories of furniture like Bookcases and Tables. Also, Technolgy is not out of the major contributing factors for profit. Infact, it is the only category where no item is sold at loss.***

# ### 2. Segment wise distribution of profit:

# **We shall now investigate the profit obtained from various segments in a barchart**

# In[39]:


segment_df = df.groupby('Segment')[['Sales','Profit']].sum()


# In[40]:


segment_df['Profit %']= segment_df['Profit']*100/segment_df['Sales']


# In[41]:


segment_df


# In[42]:


plt.xlabel('Segment')
plt.ylabel('Total Profit in that segment')
plt.title('Segment wise comparision of profit')
plt.bar(segment_df.index, segment_df['Profit']);


# **Consumer segment is the most significant segment interms of profit. Almost 1.5 times the profit of Corporate segment and more than twice of the profit of Home Office.**

# ### 3. Exploring the sales Region wise:

# **The last thing to explore is the effect of region over the sales of items:**

# In[43]:


region_df = df.groupby('Region')[['Sales','Profit']].sum()


# In[44]:


region_df['Profit %']= region_df['Profit']*100/region_df['Sales']


# **We can plot a bar chart and conclude out results.**

# In[45]:


plt.xlabel('Region')
plt.ylabel('Total Profit in that Region')
plt.title('Region wise comparision of profit')
plt.bar(region_df.index, region_df['Profit']);


# **Now, the question arises, what are the categories that bring huge difference in profit among the regions. Let us seperate these regions and examine them.**

# In[46]:


south_df=df[df['Region']=='South']
west_df=df[df['Region']=='West']


# In[47]:


south_grp=south_df.groupby('Category')['Sales'].sum()
west_grp=west_df.groupby('Category')['Sales'].sum()


# In[48]:


south_f=south_grp.to_frame()
west_f=west_grp.to_frame()


# In[49]:


south_f


# In[50]:


west_f


# ***Almost all the categories have equal contributions to profit in any region. So, the sales of all the categories must be increased in the South and Central regions to obtain more profit.***

# ## ***Asking and answering questions*** 

# ### **1.Is the superstore running in profit or loss? What percentage of profit or loss is the superstore having over its total sales?**

# In[51]:


total_profit=df['Profit'].sum()


# In[52]:


total_sales=df['Sales'].sum()


# In[53]:


percentage= total_profit/total_sales*100


# In[54]:


percentage


# ***Thus, the superstore is making a profit of 12.4% over its total sales.***

# ### 2. Which category items are sold the most interms of quantity?

# In[55]:


Category_df=df.groupby('Category')['Quantity'].sum()


# In[56]:


Category_df


# ***Office supplies items are sold the most interms of quantity.***

# ### 3.What amount of loss can be avoided if some of the items in the store can be discarded from selling?

# **The idea is to find out the overall loss occuring due to some of the items. If we can discard those items which are leading for the loss, we can acheive greater profits on overall.**

# In[57]:


loss_df = df[df['Profit']<0]


# In[58]:


total_loss=loss_df['Profit'].sum()


# In[59]:


total_loss


# ***Thus, it is possible to avoid loss amount around one and half lakh if certain items are discarded from selling.***
