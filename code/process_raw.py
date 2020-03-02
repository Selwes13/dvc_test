# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:08:09 2020

@author: Sam
"""

import pandas as pd
#%%
df = pd.read_csv("../data/grades.csv")

#%%
df_norm = df.melt(id_vars=['Name'])
df_norm

#%%
df.to_csv("../data/grades_normal.csv")