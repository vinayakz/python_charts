import pandas as pd
from matplotlib import pyplot as plt
fifa = pd.read_csv('fifa_data.csv')
fifa.Weight= [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]
#ggplot
plt.style.use('default')

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa.loc[(fifa.Weight >=125) & (fifa.Weight < 150)].count()[0]
medium = fifa[(fifa.Weight >150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa[(fifa.Weight >=175) & (fifa.Weight <200)].count()[0]
heavy = fifa[(fifa.Weight >=200)].count()[0]

weights = [light,light_medium, medium,medium_heavy,heavy]
labels = ['Under 125', '125-1520', '150-175','175-200', 'over 200']

explode = (.4,.2,0,0,.4)
plt.title('Weight Distribution of FIFA players (in lbs)')

plt.pie(weights, labels = labels,autopct='%.2f %%', pctdistance=0.8, explode=explode)
plt.show()