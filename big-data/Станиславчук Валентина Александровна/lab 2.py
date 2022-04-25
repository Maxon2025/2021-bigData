import pandas as pd
import matplotlib.pyplot as plt

battles = pd.read_csv('battles.csv', delimiter=',')
battles['attacker_king_abs'] = battles['attacker_king'].str.len()
battles_abs_g = battles.groupby(['year']).sum()['attacker_king_abs']
battles_norm_g = (battles_abs_g-battles_abs_g.min()) / (battles_abs_g.max()-battles_abs_g.min())
figure_abs = plt.figure(1)
plt.plot(battles_abs_g)
figure_norm = plt.figure(2)
plt.plot(battles_norm_g)
sum_battles = pd.DataFrame({"year": battles_abs_g.index, "abs": battles_abs_g.values, "norm": battles_norm_g.values})
print(sum_battles)
plt.show()
