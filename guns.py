
# coding: utf-8

# In[2]:


import csv

data = list(csv.reader(open("guns.csv", "r")))

print(data[:5])


# In[4]:


headers = data[0]

data = data[1:]

print(headers)

print(data[:5])


# In[8]:


years = [row[1] for row in data]

year_counts = {}

for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
print(year_counts)


# In[11]:


import datetime as dt

dates = [dt.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
print(dates[:5])

date_counts = {}

for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
        
print(date_counts)


# In[12]:


sex_counts = {}
race_counts = {}

for row in data:
    if row[5] in sex_counts:
        sex_counts[row[5]] +=1
    else:
        sex_counts[row[5]] =1
    if row[7] in race_counts:
        race_counts[row[7]] +=1
    else:
        race_counts[row[7]] =1
        
print(sex_counts)
print(race_counts)
    


# In[ ]:


#So far we've learned about gun deaths between 2012-2014:
# mostly men, around 86%
#black deaths account for only 1/3 of white deaths, but they are way less in total
# total deaths per month has been relatively stable, between 2-3k


# In[13]:


census = list(csv.reader(open("census.csv","r")))
print(census)


# In[15]:


asian_census = 15159516 + 674625
mapping = {"Asian/Pacific Islander": asian_census, "Black": 40250635, 
           "Native American/Native Alaskan": 3739506,"Hispanic": 44618105,
           "White": 197318956}

race_per_hundredk = {}

for race in race_counts:
    race_per_hundredk[race] = race_counts[race]/mapping[race]*100000
    
print(race_per_hundredk)


# In[16]:


intents = [row[3] for row in data]

races = [row[7] for row in data]

homicide_race_counts = {}

for idx, race in enumerate(races):
    if intents[idx] == "Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 1
            
for race in homicide_race_counts:
    homicide_race_counts[race] = homicide_race_counts[race]/mapping[race]*100000
    
print(homicide_race_counts)


# In[ ]:


# Black are by far the most involved in Hommicide - 4x hispanic, 12x whites
# next step: look at how other parameters affect the result - like place, police

