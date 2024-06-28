#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation

years = [1897, 1926, 1939, 1959, 1970, 1979, 1989, 1999, 2009, 2021]
nationalities = ['казахи', 'русские', 'узбеки', 'украинцы', 'уйгуры', 'немцы', 'татары', 'азербайджанцы', 'корейцы', 'турки']
data = [
    [3391268, 454184, 19564, 79573, 5815, 2613, 55984, 8300, 0, 15],
    [3627612, 1275055, 129399, 860201, 2313, 51094, 79758, 10157, 42, 68],
    [2127625, 2458687, 120655, 658319, 15409, 92571, 108127, 12996, 96457, 523],
    [2794966, 3974229, 136570, 762131, 59840, 659751, 191925, 38362, 74019, 9916],
    [4161164, 5449826, 207514, 930158, 120784, 839649, 281849, 56166, 78078, 18397],
    [5289349, 5991205, 263295, 897964, 147943, 900207, 312626, 73345, 91984, 25820],
    [6534616, 6227549, 332017, 896240, 185301, 957518, 327982, 90083, 103315, 49567],
    [7985039, 4479620, 370663, 547052, 210365, 353441, 248954, 78295, 99665, 75900],
    [10096763, 3793764, 456997, 333031, 224713, 178409, 204229, 85292, 100385, 97015],
    [13497891, 2981946, 614047, 387327, 290337, 226092, 218653, 145615, 118450, 85478]
]

df = pd.DataFrame(data, columns=nationalities, index=years)

def update(num, df, ax):
    ax.clear()
    year = df.index[num]
    data = df.iloc[num]
    wedges, texts, autotexts = ax.pie(data, autopct='%1.1f%%', startangle=90, pctdistance=1.2, textprops={'fontsize': 14, 'fontname': 'Arial'})
    ax.axis('equal')
    ax.legend(wedges, nationalities, title="Национальности", loc="center", bbox_to_anchor=(1, 0.5), fontsize='x-large', title_fontsize='x-large', prop={'family': 'Arial', 'size': 17})
    ax.set_title(f'Национальный состав Казахстана - {year}', y=1.1, fontsize=25, fontname='Arial')

fig, ax = plt.subplots(figsize=(18, 14))  
ax.axis('equal')

ani = FuncAnimation(fig, update, frames=len(years), fargs=(df, ax), repeat=False, interval=2000)  # Увеличиваем время на кадр

ani.save('national_composition_kazakhstan.gif', writer='pillow', fps=0.5)

plt.show()


# In[ ]:




