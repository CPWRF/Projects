# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
plt.style.use('bmh')
df = pd.read_excel('MK3_PR_tumble.xlsx')
df2 = pd.read_excel('MK3_PR_tumble_raw.xlsx')
# %%
plt.figure(dpi=150)
plt.title('MK3 tumble_cycle vs Sonar_Tx_RMS_AVG')
g = sns.lineplot(data=df, x='Tumble_Cycle', y='Sonar_Tx_RMS_AVG', hue='SerialNumber', 
                 marker='o', palette='Set1');
plt.fill_between(x=[40,70], y1=[2000], color='gray', alpha=0.3)
plt.ylim([800,2000])
plt.axhline(y=880, color='red', ls='--', alpha=0.3)
g.text(0,900, 'LSL', color='red', alpha=0.6)
g.text(42,1100, 'Clean water tank', color='k', alpha=0.6)