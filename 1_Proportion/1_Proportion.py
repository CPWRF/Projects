#%%
from statsmodels.stats.proportion import proportions_ztest

# %%
count1 = 5
nobs1 = 14
count2 = 0
nobs2 = 7

stat, pval = proportions_ztest([count1, count2], [nobs1, nobs2], alternative='smaller')

print(f"Test statistic: {stat:.4f}")
print(f"P-value: {pval:.4f}")