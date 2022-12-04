import matplotlib.pyplot as plt
import pandas as pd

df_a_star = pd.read_csv("A_star_results.csv", header = 0)

print(df_a_star)

df_greedy = pd.read_csv("Greedy_best_first_results.csv", header = 0)

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

plt.plot(df_greedy.columns, df_greedy.iloc[1], label="Greedy")
plt.plot(df_a_star.columns, df_a_star.iloc[1], label ="A star")
plt.title('N VS Steps_to_find_solution', fontsize=14)
plt.xlabel('N')
plt.ylabel('Steps_to_find_solution')
# plt.xscale("log")
# plt.yscale("log")
plt.legend()
plt.savefig("graphs/N VS Steps_to_find_solution.png")
plt.show()

plt.plot(df_greedy.columns, df_greedy.iloc[2], label="Greedy")
plt.plot(df_a_star.columns, df_a_star.iloc[2], label ="A star")
plt.title('N VS Visited_states', fontsize=14)
plt.xlabel('N')
plt.ylabel('Visited_states')
# plt.xscale("log")
# plt.yscale("log")
plt.legend()
plt.savefig("graphs/N VS Visited_states.png")
plt.show()

