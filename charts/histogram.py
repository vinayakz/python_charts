import pandas as pd
from matplotlib import pyplot as plt
bins = [40,50,60,70,80,90,100]
fifa = pd.read_csv('fifa_data.csv')

plt.hist(fifa.Overall, bins=bins,color='#fcba03')
plt.ylabel('Number of players',fontdict={"fontweight":'bold'})
plt.xlabel('Skills Level',fontdict={"fontweight":'bold'})
plt.title("Distribution of player Skill in FIFA 2018",fontdict={'fontweight':'bold'})
plt.show()