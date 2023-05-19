#!/usr/bin/env python
# coding: utf-8

# ### Download the datasets
# 
# This assignment requires you to have these three tables populated with a subset of the whole datasets.
# 
# In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the links below to download and save the datasets (.CSV files):
# 
# - <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv" target="_blank">Chicago Census Data</a>
# 
# - <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv" target="_blank">Chicago Public Schools</a>
# 
# - <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv" target="_blank">Chicago Crime Data</a>
# 
# **NOTE**: For the learners who are encountering issues with loading from .csv in DB2 on Firefox, you can download the .txt files and load the data with those:
# 
# - <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.txt" target="_blank">Chicago Census Data</a>
#     
# - <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.txt" target="_blank">Chicago Public Schools</a>
#   
# - <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.txt" target="_blank">Chicago Crime Data</a>
# 
# **NOTE:** Ensure you have downloaded the datasets using the links above instead of directly from the Chicago Data Portal. The versions linked here are subsets of the original datasets and have some of the column names modified to be more database friendly which will make it easier to complete this assignment.
# 

# ##### Now open the Db2 console, open the LOAD tool, Select / Drag the .CSV file for the first dataset, Next create a New Table, and then follow the steps on-screen instructions to load the data. Name the new tables as follows:
# 
# 1.  **CENSUS_DATA**
# 2.  **CHICAGO_PUBLIC_SCHOOLS**
# 3.  **CHICAGO_CRIME_DATA**
# 

# ### Connection to the database

# In[22]:


# These libraries are pre-installed in SN Labs. If running in another environment please uncomment lines below to install them:
get_ipython().system('pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3')
# Ensure we don't load_ext with sqlalchemy>=1.4 (incompadible)
get_ipython().system('pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24')
get_ipython().system('pip install ipython-sql')


# In[23]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[24]:


get_ipython().run_line_magic('sql', 'ibm_db_sa://rrc19071:OiyY9v7qTKHe0bQA@19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:30699/bludb?security=SSL')


# ## Problems
# 
# ### Problem 1
# 
# ##### Find the total number of crimes recorded in the CRIME table.
# 

# In[25]:


get_ipython().run_cell_magic('sql', '', 'select count (*) from CHICAGO_CRIME_DATA\n')


# ### Problem 2
# 
# ##### List community areas with per capita income less than 11000.
# 

# In[28]:


get_ipython().run_cell_magic('sql', '', 'select COMMUNITY_AREA_NAME from CENSUS_DATA where PER_CAPITA_INCOME <11000\n')


# ### Problem 3
# 
# ##### List all case numbers for crimes  involving minors?(children are not considered minors for the purposes of crime analysis)
# 
# 

# In[29]:


get_ipython().run_cell_magic('sql', '', "select CASE_NUMBER,PRIMARY_TYPE DESCRIPTION from CHICAGO_CRIME_DATA where DESCRIPTION like '%MINOR%' or PRIMARY_TYPE like '%MINOR%'\n")


# ### Problem 4
# 
# ##### List all kidnapping crimes involving a child?
# 

# In[30]:


get_ipython().run_line_magic('sql', "select * from CHICAGO_CRIME_DATA where primary_type like '%KIDNAP%' and description like '%CHILD%'")


# ### Problem 5
# 
# ##### What kinds of crimes were recorded at schools?
# 

# In[31]:


get_ipython().run_line_magic('sql', "select distinct(primary_type) from CHICAGO_CRIME_DATA where location_description like '%SCHOOL%'")


# ### Problem 6
# 
# ##### List the average safety score for each type of school.
# 

# In[70]:


get_ipython().run_cell_magic('sql', '', 'SELECT ELEMENTARY__MIDDLE__OR_HIGH_SCHOOL, AVG(SAFETY_SCORE) AVERAGE_SAFETY_SCORE from CHICAGO_PUBLIC_SCHOOLS group by ELEMENTARY__MIDDLE__OR_HIGH_SCHOOL;\n')


# ### Problem 7
# 
# ##### List 5 community areas with highest % of households below poverty line 
# 

# In[42]:


get_ipython().run_line_magic('sql', 'select community_area_name ,percent_households_below_poverty from census_data order by percent_households_below_poverty desc limit 5')


# ### Problem 8
# 
# ##### Which community area is most crime prone?
# 

# In[43]:


get_ipython().run_line_magic('sql', 'select community_area_number ,count(*) as frequency from CHICAGO_CRIME_DATA group by community_area_number order by frequency desc limit 1')


# Double-click **here** for a hint
# 
# <!--
# Query for the 'community area number' that is most crime prone.
# -->
# 

# ### Problem 9
# 
# ##### Use a sub-query to find the name of the community area with highest hardship index
# 

# In[44]:


get_ipython().run_line_magic('sql', 'select community_area_name from CENSUS_DATA where hardship_index = (Select max(hardship_index) from CENSUS_DATA)')


# ### Problem 10
# 
# ##### Use a sub-query to determine the Community Area Name with most number of crimes?
# 

# In[45]:


get_ipython().run_line_magic('sql', 'select community_area_name from census_data where community_area_number = (select community_area_number from CHICAGO_CRIME_DATA where community_area_number =25 limit 1)')


# Copyright © 2020 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork22-2022-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
