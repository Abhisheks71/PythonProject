
# coding: utf-8

# In[69]:

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random
get_ipython().magic('matplotlib inline')


# In[70]:

PokemonDf=pd.read_csv('pokemon/Pokemon.csv')


# In[71]:

PokemonDf.head(200000)


# In[72]:


PokemonDf.describe()
PokemonDf.Name.value_counts()


# In[73]:

gx=PokemonDf['Generation'].value_counts().plot.bar(width=0.5)
for b in gx.patches:
    gx.annotate(b.get_height()+1,(b.get_x(),b.get_height()+1))


# In[74]:

import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls


# In[75]:

Pokemon_all=pd.concat([PokemonDf['Attack'],PokemonDf['HP']])
Pokemon_all


# In[76]:

Pokemon_all=pd.concat([PokemonDf['Attack'],PokemonDf['HP']])
Pokemon_all=Pokemon_all.value_counts().reset_index()
Pokemon_all.columns=['Bark','Defense']
Pokemon_all


# In[77]:

Pokemon_all.plot()


# In[ ]:




# In[78]:

Pokemon_all['Protect']=PokemonDf['Defense'].value_counts().reset_index()['Defense']
Pokemon_all.set_index('Bark',inplace=True)
Pokemon_all


# In[79]:

graph1=go.Bar(x=Pokemon_all.index,y=Pokemon_all['Defense'],name='Defense')
graph2=go.Bar(x=Pokemon_all.index,y=Pokemon_all['Protect'],name='Total Protect1')
data=[graph1,graph2]
layout=go.Layout(barmode='stack')
fig=go.Figure(data=data,layout=layout)
py.plot(fig,filename='stacked-bar.html')


# In[ ]:




# In[ ]:



