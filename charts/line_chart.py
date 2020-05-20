import pandas as pd
from matplotlib import pyplot as plt
gas = pd.read_csv('gas_prices.csv')
plt.figure(figsize=(8,5))

plt.plot(gas.Year, gas.USA, 'r.-',label="USA")
plt.plot(gas.Year, gas.Canada, 'b.-',label="Canada")
plt.plot(gas.Year, gas['South Korea'], 'g.-',label="South Korea")
plt.plot(gas.Year, gas.Australia, 'y.-',label="Australia")

plt.title("USA vs Canada Gas prices", fontdict={'fontweight':'bold','fontsize':22})
plt.ylabel("Dollars/Gallon",fontdict={'fontweight':'bold'})
plt.legend()

plt.xticks(gas.Year[::3].tolist()+[2011])
plt.savefig('gas.png', dpi=300)
plt.show()