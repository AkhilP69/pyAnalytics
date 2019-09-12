#Topic:
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars
catcols = ['cyl','vs','am','gear','carb']

catcols
df[catcols] = df[catcols].astype('category')
dir(df)
df.dtypes
df.groupby(catcols).size().plot(kind='bar')
df.groupby(catcols).size().plot(kind='bar')
