# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:08:09 2020

@author: Sam
"""
#%%
import os
import pandas as pd
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())
#%%
df = pd.read_csv("..\\data\\grades.csv")

#%%
df_norm = df.melt(id_vars=['Name'])
df_norm

#%%
df.to_csv("../data/grades_normal.csv")

# %%
