#!/usr/bin/env python
# coding: utf-8

# In[1]:


africaCases = {
    "country": ["Nigeria", "Seychelles", "Zambia", "Kenya", "Uganda"],
    "total": [500, 200, 900, 400, 300 ],
    "active": [200, 50, 400, 100, 120],
    "discharged": [250, 190, 400, 280, 150],
    "death": [50, 10, 100, 20, 30]
}


# In[13]:


descriptive = {
    "country": ["Nigeria", "Seychelles", "Zambia", "Kenya", "Uganda"],
    "descriptive":["Nigeira is fighting the virus back to back", "Seychelles conquered the battle", "Zambia is getting close to winning if they have resources", "Kenya have high hope about overcoming", "Uganda are ready to kick out any Chinese man now"]
}


# In[14]:


import pandas as pd


# In[ ]:


import sys


# In[15]:


covid = pd.DataFrame(africaCases)


# In[16]:


descrip = pd.DataFrame(descriptive)


# In[17]:


descrip


# In[34]:


descrip["country"].values.tolist().index("Nigeria")


# In[4]:


covid


# In[7]:


covid['country'] == 'Nigera', 'total'


# In[11]:


covid.loc[0]


# In[ ]:


question = True


# In[40]:


while question:
    choice = input("Which Africa country do you wish to know the state of covid-19: ")
    if choice == "Nigeria":
        print(covid.loc[0])
    elif choice == "Seychelles":
        print(covid.loc[1])
    elif choice == "Zambia":
        print(covid.loc[2])
    elif choice == "Kenya":
        print(covid.loc[3])
    elif choice =="Uganda":
        print(covid.loc[4])
    elif choice =="":
        break
    choices = input("Do you need a descriptive report of this country?: ")
    if choices == "yes":
        countryI = descrip["country"].values.tolist().index(choice)
        print(descrip.loc[countryI])
    elif choices == "":
        break
print("Thanks for your interest")
    
        
        
        
    


# In[ ]:





# In[ ]:




