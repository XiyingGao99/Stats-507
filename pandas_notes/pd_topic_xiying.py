# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Problem Set 4
# *Xiying Gao(xiying@umich.edu)*
# *Oct 14, 2021*

# # Q0. Topics in Pandas

# ## Table Styler

# - Styler object can manipulate many parameters of a table, including colors, fonts, borders, background, etc. 
# - The .style attribute is a Styler object.
# - The Styler actually creates an HTML <table> and leverages CSS styling language, which allows a lot of flexibility and even enables web developers to integrate DataFrames into their exiting user interface designs.

# +
import pandas as pd
import numpy as np

df = pd.DataFrame([[1512.0, 1222, 1342.0, np.nan],
                   [245, 393, 608, 521]],
                  index=pd.Index(['Keeping Pets', 'Playing Guitar'], 
                                 name='Hobbies:'),
                  columns=pd.MultiIndex.from_product([['Grade 10', 'Grade 11'],
                                                      ['Girl','Boy']], 
                                                     names=['Grade:', 
                                                            'Gender:']))
df.style 
#The output below looks very similar to the standard DataFrame HTML represen-
#tation. But the HTML here has already attached some CSS classes to each cell
# -

# ## Table Styler

# - Use `.style.format()` to control the display values' formats
# - Use `.style.format.hide_columns()` to hide some data and format the values.

s = df.style.format(formatter={('Grade 10', 'Girl'): "{:.2f}",
                               ('Grade 11', 'Girl'): 
                               lambda x: "# {:,.1f}".format(x*10)
                              }) # specify data format for each column
#s
s.format('{:.0f}', na_rep="Missing").hide_columns([('Grade 11', 'Girl')])
s

# ## Table Styler

# - There are some built-in functions in Styler object.
# - Use `highlight` function to highlight max/min/null value.
# - Use `.style.bar()` to include “bar charts” in your DataFrame.
# - Use `subset` attribute to apply format on the subset of the DataFrame.

df.style.highlight_max() #default color is yellow
df.style.highlight_min() #default color is yellow
df.style.highlight_null(null_color='yellow') #default color is red
s1 = df.style.bar(subset=['Grade 10'], align='mid', color=['#d65f5f'])
s1


# ## Table Styler

# - Use `style.applymap()` to apply changes to each element in the DataFrame.
# - Use `style.apply()` to apply changes to row/column/table wise in the DataFrame.  For columnwise use axis=0, rowwise use axis=1, and for the entire table at once use axis=None.
# - You can define your own function as an attribute in `apply` functions above.

# +
def style_lessthan600(v, props=''):
    return props if v < 600 else None
s1 = df.style.applymap(style_lessthan600, props='color:red;') 

def highlight_max(s, props=''):
    return np.where(s == np.nanmax(s.values), props, '')
s1.apply(highlight_max, props='color:white;background-color:darkblue;', axis=0)
s1
# -
