import matplotlib.pyplot as plt
import pandas as pd

df_20 = pd.read_csv("results/results20.csv", header = 0)
df_100 = pd.read_csv("results/results100.csv", header = 0)
df_500 = pd.read_csv("results/results500.csv", header = 0)
df_1000 = pd.read_csv("results/results1000.csv", header = 0)
df_5000 = pd.read_csv("results/results5000.csv", header = 0)

print(df_20.head())

'''
plt.plot(df_greedy.columns, df_greedy.iloc[0], label="Greedy")
plt.plot(df_a_star.columns, df_a_star.iloc[0], label ="A star")
plt.title('N VS Weights', fontsize=14)
plt.xlabel('N')
plt.ylabel('Weights')
# plt.xscale("log")
# plt.yscale("log")
plt.legend()
plt.savefig("graphs/N VS Weights.png")
plt.show()
'''
