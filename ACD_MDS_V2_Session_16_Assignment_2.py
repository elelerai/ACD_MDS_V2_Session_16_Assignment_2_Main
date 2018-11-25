# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 09:30:29 2018

@author: Eliud Lelerai
"""

import numpy as np
import pandas as pd

# Creating the dataframe


height_data={'id':list(range(6)),'tree_height':[3, 21, 98, 203, 17, 9]}

height_df=pd.DataFrame(height_data)

height_df.dtypes



# getting the height variance.

print((height_df['tree_height']).std())

height_var=(height_df['tree_height']).std()**2